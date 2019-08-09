# 1. Code Reviews

The first thing I review is the comments in a script or notebook. Comments provide readability for your code even if the person reading it isn't familiar with the modules/libraries used in it. Using whitespace and indenting wisely is important to code. Giving your code a bit of a visual structure makes it look much less confusing. It's always useful to have another set of eyes look through your code. Usually, by the time you're done building a script or package you've forgotten which parts were confusing and perhaps didn't comment clearly enough to communicate your work.

# 2. Dockers

Dockers are extraordinarily useful because they allow a program/app/whatever-you-want to run on any computer regardless of the native Operating System. In a Dockerfile, you can specify which deoendencies your app requires. Then, using that Dockerfile you can build an isolated container with those exact dependencies. Running the app in a container rather than straight on the machine saves you the trouble of completely reconfiguring a machine to use one app.

Docker containers are a little heavier than a virtual environment, but a little lighter than a virtual machine. This makes them ideal for software development and deployment.