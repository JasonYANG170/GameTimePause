[简体中文](README.md) | [English](README_en.md)

<div align="center">
    <h1>GameTimePause — accelerator time balance pause script</h1>
    <img src="https://img.shields.io/github/license/JasonYANG170/GameTimePause?label=License&style=for-the-badge">
    <img src="https://img.shields.io/github/commit-activity/w/JasonYANG170/GameTimePause?style=for-the-badge">
	<img src="https://img.shields.io/github/languages/count/JasonYANG170/GameTimePause?logo=python&style=for-the-badge">
	<br>
    	<a href="https://discord.com/invite/az3ceRmgVe"><img alt="Discord" src="https://img.shields.io/discord/978108215499816980?style=social&logo=discord&label=echosec"></a>
  <br>

This is a Github Actions automated timing script based on Python language
  
<br>

</div>

## Support platform
- ✅Leigod Accelerator
- ✅ NN accelerator

If you use other time-based accelerators, please raise issues with me.
## Tutorial
1. Please Fork this project first.

2. In your repository, open Settings → Secrets → Actions and select New repository secret to add the variables below:
    - PHONE (fill in your registered mobile phone number)
    - PASSWORD (fill in your account password)
    - TOKEN (optional, fill in the Token of PUSHPLUS)
3. Open your repository's Actions tab, then click the green "I understand my workflows, go ahead and enable them" button to enable Actions.

4. Find "pause" in the left sidebar and click it, then click "Enable workflow" on the right side to enable this action

5. The default schedule runs daily at 03:00 (UTC+8). GitHub Actions may delay execution by around 20 minutes. To change the schedule, edit `- cron: '0 19 * * *'`; use https://crontab.guru/ to generate an expression.

