 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.



UI / Screenshots
=================
The Airflow UI makes it easy to monitor and troubleshoot your data pipelines.
Here's a quick overview of some of the features and visualizations you
can find in the Airflow UI.


.. _ui:home:

Home Page
.........

Gives an overview about recent running dags and tasks and basic system health.

------------

.. image:: img/ui-dark/home.png

------------


Dags View
.........

List of the dags in your environment, and a set of shortcuts to useful pages.
You can see exactly how many tasks succeeded, failed, or are currently
running at a glance.

In order to filter dags (e.g. by team), you can add tags in each DAG.
The filter is saved in a cookie and can be reset by the reset button.
For example:

.. code-block:: python

   dag = DAG("dag", tags=["team1", "sql"])


------------

.. image:: img/ui-dark/dags.png

------------


.. _ui:assets-view:

Asset View
..........

A combined listing of the current assets and details how they are produced and consumed by dags.

Clicking on any asset detail in the list will show it and its relationships, and filter the list to show the recent history of task instances that have updated that dataset and whether it has triggered further DAG runs.

------------

.. image:: img/ui-dark/assets.png

------------

.. image:: img/ui-dark/assets_graph.png

------------


Grid View
.........

A bar chart and grid representation of the DAG that spans across time.
The top row is a chart of DAG Runs by duration,
and below, task instances. If a pipeline is late,
you can quickly see where the different steps are and identify
the blocking ones.

The overview panel on the right provides fast access to recently failed tasks and logs.

The overview includes the Dag runtime for the last execution to find outliers.

------------

.. image:: img/ui-dark/grid.png

------------

The details panel will update when selecting a DAG Run by clicking on a duration bar:

.. image:: img/ui-dark/grid_run_details.png

Or selecting a Task Instance by clicking on a status box:

.. image:: img/ui-dark/grid_instance_details.png

Or selecting a Task across all runs by click on the task_id.

This also plots the duration of your different tasks over the past N runs. This view lets
you find outliers and quickly understand where the time is spent in your
DAG over many runs.

.. image:: img/ui-dark/grid_task_details.png

Manual runs are indicated by a play icon (just like the Trigger DAG button).
Asset triggered runs are indicated by a database icon.
Normal scheduled runs have no indicator.
If a backfill was used to create the DAG run, it will be indicated by a arrow icon:

.. image:: img/ui-dark/run_types.png

Task groups are indicated by a caret and can be opened or closed:

.. image:: img/ui-dark/grid_task_group.png

Mapped Tasks are indicated by square brackets and will show a table of each mapped task instance in the Mapped Tasks panel:

.. image:: img/ui-dark/grid_mapped_task.png

------------


.. _ui:graph-view:

Graph View
..........

The graph view is perhaps the most comprehensive. Visualize your DAG's
dependencies and their current status for a specific run.

------------

.. image:: img/ui-dark/graph.png

------------

If you use the options to display external dependencies, you can follow asset conditions and events.

------------

.. image:: img/ui-dark/graph_dependencies.png

------------

Variable View
.............

The variable view allows you to list, create, edit or delete the key-value pair
of a variable used during jobs. The value of a variable will be hidden if the key contains
any words in ('password', 'secret', 'passwd', 'authorization', 'api_key', 'apikey', 'access_token')
by default, but can be configured to show in cleartext. See :ref:`security:mask-sensitive-values`.

------------

.. image:: img/ui-dark/variable_hidden.png

------------

Code View
.........

Transparency is everything. While the code for your pipeline is in source
control, this is a quick way to get to the code that generates the DAG and
provide yet more context.

------------

.. image:: img/ui-dark/code.png

Backfill
........

If runs in your scheduled Dag are missing you can use the backfill option in the UI to re-run missing
executions for a selective time interval.

------------

.. image:: img/ui-dark/backfill.png

Trigger Form
............

If you trigger a manual DAG run with the arrow-button, a form is displayed.
The form display is based on the DAG Parameters as described in :doc:`core-concepts/params`.

------------

.. image:: img/ui-dark/trigger-dag-tutorial-form-1.png

Events
......

See all events related to a DAG.

------------

.. image:: img/ui-dark/events.png

------------
