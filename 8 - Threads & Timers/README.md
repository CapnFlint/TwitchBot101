# Threads and Timers

## Purpose
Everything we have done so far has been single threaded. Each procedure completes
before another can begin. Anything that isn't currently being processed is considered
to be "Blocking", which means that action is blocked while it waits for it's turn.

Threading is a method to break up an application into multiple "threads", which
can each be processed concurrently. This allows one thread to be held up waiting
for something, while another thread can continue working away.

In this section, we will have a brief introduction to threading, show how to create
a new thread, and combine it with timers to create timed events.

## Notes
* Class Extension
* Daemon vs Non-Daemon threads

## Useful Links

* https://docs.python.org/2/library/threading.html - High level Python Threading Interface
* https://docs.python.org/2/library/thread.html - Low level Python Thread Documentation
