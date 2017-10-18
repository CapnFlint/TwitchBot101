# API Overview

## Purpose
This section gives you a basic overview of the Twitch API's, how they work, and
what is currently available.

*Note: I will be referencing v5 of the API. This version
is "deprecated", however will be functional until the end of 2018. The newer API
is functional, but is still being developed so far as functionality, and currently
cannot perform every function of the v5 API.*

## Notes
Two API's Exist:
* https://api.twitch.tv/kraken - Main Twitch API (client Id required)
* https://tmi.twitch.tv/ - Twitch message interface. Used to get list of current
viewers in chat

Client ID is always required for making requests. Privileged requests also require
an oauth authentication token.

Key Endpoints:
* Channels - Retrieve and update data about a specified channel, including all
followers, subscribers, teams etc.
* Streams - Retrieve information about live streams, including start time, viewcount,
current game etc.
* Users - Retrieve information about a given user, such their logo, creation date,
followed channels, and their subscription status to a given channel. Also perform
user level actions, like following a given channel.

## Useful Links
* https://dev.twitch.tv/docs/v5 - Twitch API Documentation
