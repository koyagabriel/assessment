# Debugging

### Expectation
The Developer is able to use their knowledge to facilitate root cause analysis across integrated components developed by the members of their team and external teams. They have the ability to diagnose problems by reverse engineering inherited code bases.

### Justification
During the time I was contirbuting to Mozilla Balrog project, I picked up a bug ticket titled ` Make the order of enacting changes predictable`. In order to fix the bug, I had to run a root cause analysis which basically invloved identifying the problem and collecting valid data needed to better understand the issue. since it's an open source project, I had to ensure I understood how different components within the system are integrated before concluding on the best approach towards fixing the bug.

After fixing the bug and writing tests for it, other tests from other components were failing which led to a reiteration of running a root cause analysis on why they were failing and fixing them accordingly.

[Link to the bug fix](https://github.com/mozilla/balrog/pull/291/files)