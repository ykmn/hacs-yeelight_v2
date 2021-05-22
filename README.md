# HACS repository for Home Assistant custom component for Yeelight bulbs

This repository allows to add custom component for Yeelight lamps ([Silvest89/yeelight_v2](https://github.com/Silvest89/yeelight_v2)) to Home Assistant via HACS.

[Yeelight_v2](https://github.com/Silvest89/yeelight_v2) is a custom component for Home Assistant that can be used as an alternative Yeelight integration for Home Assistant. It currently supports SSDP as a fallback for the get_prop method. The miio protocol has also been implemented. If a miio_token is provided then the miio protocol will be used to communicate with the bulb (no LAN Control needed)

![Yeelight Logo](https://brands.home-assistant.io/_/yeelight/logo.png)

Readme, docs and support at [Silvest89/yeelight_v2](https://github.com/Silvest89/yeelight_v2)


# Installation using HACS

1. Install [HACS](https://hacs.xyz/docs/installation/prerequisites)

2. Open HACS / Integrations / Custom Repositories

3. Add https://github.com/ykmn/hacs-yeelight_v2 as Integration

4. Click Install

[![hacs][hacsbadge]][hacs]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/hacs-true-success.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/twelve
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-blue.svg?style=for-the-badge