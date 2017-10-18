# Twitch API

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
* Registering an app to use the API
* Authenticating to the API
* Requesting data
* PubSub

## Useful Links

* https://dev.twitch.tv/dashboard/apps - App Dashboard, for registering your Bot
