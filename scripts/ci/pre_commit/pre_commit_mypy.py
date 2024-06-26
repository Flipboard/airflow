#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.resolve()))

from common_precommit_utils import (
    console,
    filter_out_providers_on_non_main_branch,
    initialize_breeze_precommit,
    run_command_via_breeze_shell,
)

initialize_breeze_precommit(__name__, __file__)

files_to_test = filter_out_providers_on_non_main_branch(sys.argv[1:])
if files_to_test == ["--namespace-packages"]:
    print("No files to tests. Quitting")
    sys.exit(0)

res = run_command_via_breeze_shell(
    [
        "/opt/airflow/scripts/in_container/run_mypy.sh",
        *files_to_test,
    ],
    warn_image_upgrade_needed=True,
    extra_env={
        "INCLUDE_MYPY_VOLUME": "true",
    },
)
if res.returncode != 0:
    upgrading = os.environ.get("UPGRADE_TO_NEWER_DEPENDENCIES", "false") != "false"
    if upgrading:
        console.print(
            "[yellow]You are running mypy with the image that has dependencies upgraded automatically."
        )
    flag = " --upgrade-to-newer-dependencies" if upgrading else ""
    console.print(
        "[yellow]If you see strange stacktraces above, "
        f"run `breeze ci-image build --python 3.8{flag}` and try again. "
        "You can also run `breeze down --cleanup-mypy-cache` to clean up the cache used. "
        "Still sometimes diff heuristic in mypy is behaving abnormal, to double check you can "
        "call `breeze static-checks --type mypy-[dev|core|providers|docs] --all-files` "
        'and then commit via `git commit --no-verify -m "commit message"`. CI will do a full check.'
    )
sys.exit(res.returncode)
