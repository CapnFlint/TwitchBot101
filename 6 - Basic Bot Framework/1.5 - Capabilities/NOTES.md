# capabilities

## Purpose

In addition to the default data received when connecting to the Twitch IRC service,
it is possible to register a number of optional additional capabilities. These
capabilities allow your bot to receive more data and metadata, which will be Useful
when creating more interesting functionality.

## Notes

The available capabilities are:
* **Membership** - This capability registers for membership state event data, including
notifications when users join or leave the channel.
* **Tags** - This capability registers to receive additional Tag metadata for messages
in the channel. This gives is a significant amount of data about a user or message,
such as ban reasons, emotes used, and the subscriber status of a user.
* **Commands** - This capability registers to receive basic notifications for general
events in chat, such as server notices, usernotice messages and hosts.

## Useful Links

* https://dev.twitch.tv/docs/irc - Twitch IRC Documentation
