[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c17f50693da4c008501cdb996f9ba0f)](https://www.codacy.com/gh/dream-alpha/TestCockpit/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dream-alpha/TestCockpit&amp;utm_campaign=Badge_Grade)

<a href="https://gemfury.com/f/partner">
  <img src="https://badge.fury.io/fp/gemfury.svg" alt="Public Repository">
</a>

# TestCockpit (TST)
## Features
- TST is a plugin for regression testing the basic functionality of the Cockpit series plugins e.g. MovieCockpit.

## Limitations
- TST supports DreamOS only
- TST is being tested on DM 920 and DM ONE only
- TST supports FHD (Full HD) skins only

## Installation
To install TestCockpit execute the following command in a console on your dreambox:
- apt-get install wget (only required the first time)
- wget https://dream-alpha.github.io/MovieCockpit/testcockpit.sh -O - | /bin/sh

The installation script will also install a feed source that enables a convenient upgrade to the latest version with the following commands or automatically as part of a DreamOS upgrade:
- apt-get update
- apt-get upgrade

## Links
- Package feed: https://gemfury.com/dream-alpha
