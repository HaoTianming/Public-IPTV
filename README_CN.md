<div align="center"><h1>用于 Cloudstream 的 IPTV 扩展/插件</h1></div>
<div align="center"><h2><a href="https://github.com/HaoTianming/Public-IPTV#dmca">DMCA 通知</a></h2></div>

<br/>

<p align="center">
  <a href="https://github.com/HaoTianming/Public-IPTV/raw/refs/heads/master/LICENSE"><img src="https://www.gnu.org/graphics/agplv3-with-text-162x68.png" /></a><br/><br/>
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=kotlin,androidstudio,gradle,github,githubactions&theme=light&perline=5" />
  </a>
</p>

<br/>

# **继续之前请阅读**

> [!NOTE]
> - ### 由于扩展/插件的操作机制，本仓库***不接受***也***不会接受***任何类型的***内容请求***。***请勿***就此开启任何 issue。
> - ### ***请勿开启***关于某些频道或视频流无法正常工作或加载的 issue。由于我们***不托管、重新托管、流式传输、重新流式传输、存储或控制***任何媒体、文件或视频流，或任何可能通过扩展/插件功能访问的内容，因此我们无法控制哪些工作，哪些无法工作。
> - ### 某些流/频道在没有连接到与播放列表国家匹配的***VPN服务器***的情况下***将不会***工作。

> [!CAUTION]
> ## 本仓库仅用于教育和交流目的，请勿以任何商业目的使用。
> ### <ul><li> 通过安装和使用此扩展，您承认开发者对通过扩展/插件访问的内容不承担任何责任。请注意，此类内容可能来源于未经验证或不合法的渠道。 </li></ul>
> ### <ul><li> 作为最终用户，确保合法使用此扩展/插件是您唯一的责任，我们强烈建议您核实通过扩展/插件访问的任何内容是否符合您所在司法管辖区适用的法律法规，包括但不限于知识产权法律。 </li></ul>
> ---
> ### <ul><li> 若您持有任何版权、代表版权持有人，或对通过此扩展/插件访问的内容有任何疑问，我们强烈建议您查阅 [README 中的 DMCA 部分](https://github.com/HaoTianming/Public-IPTV#dmca) 获取重要信息。 </li></ul>

<br/>

<h1>DMCA</h1>

> [!IMPORTANT]  
> ### 我们特此声明：
> #### <ul><h3> 功能描述： </h3> <li> 此扩展/插件专门用于帮助用户定位和访问各种公共互联网[视频]流。它们的操作机制类似于传统网络浏览器及其内置视频播放器，因为本仓库从众多公开的 GitHub 仓库中抓取和解析 M3U 播放列表文件并提供给用户。因此，我们坚信本仓库中的扩展和插件以及仓库本身不违反数字千年版权法 (DMCA) 的相关规定。 </li></ul>
> #### <ul><h3> 非托管免责声明： </h3> <li> 这些扩展/插件的所有者和开发者以及仓库 [HaoTianming/Public-IPTV](https://github.com/HaoTianming/Public-IPTV) 明确声明，他们不托管、重新托管、流式传输、重新流式传输、存储或控制任何可能通过扩展/插件功能访问的媒体、文件或视频流，或任何其他内容。因此，扩展/插件及仓库 [HaoTianming/Public-IPTV](https://github.com/HaoTianming/Public-IPTV) 的所有者/开发者对从上述公共 GitHub 仓库（详见功能描述）中抓取的 M3U 播放列表所派生的任何文件、媒体或流的内容、可用性或合法性不承担任何责任。 </li></ul>
> #### <ul><h3> 责任限制： </h3>  <li> 扩展/插件和仓库 [HaoTianming/Public-IPTV](https://github.com/HaoTianming/Public-IPTV) 的所有者及开发者对内容使用不当不承担任何责任，无论是在扩展/插件中、本 GitHub 仓库中还是在外部环境中。此外，对于通过使用扩展/插件和本 GitHub 仓库可能传播的任何内容，所有者/开发者也不承担任何责任。 </li></ul>
> #### <ul><h3> 用户责任： </h3> <li> 终端用户有责任确保遵守其所在司法管辖区适用的所有法律法规，包括但不限于知识产权法。 </li></ul>
> #### <ul><h3> 侵权问题： </h3> <li> 扩展/插件的所有者/开发者以及仓库 [HaoTianming/Public-IPTV](https://github.com/HaoTianming/Public-IPTV) 对任何涉嫌侵权行为不承担法律责任。如果任何一方认为其知识产权受到侵犯，我们建议您联系相关 GitHub 仓库的所有者，因为扩展/插件和本 GitHub 仓库正是从这些仓库抓取数据，以及联系引用于这些仓库中的各个互联网流的托管方。我们抓取的 GitHub 仓库（及其文件）列表已为您整理在 [这里](https://github.com/HaoTianming/Public-IPTV/blob/main/.github/pyscripts/urls.json)。</li></ul>
> ### 谢谢。

<br/>

# 致谢及归属：

- ## 特别感谢：
  - ### [Phisher98](https://github.com/Phisher98)，感谢他的支持及 IPTV 扩展模板 QuickIPTV，该模板已在此扩展中使用 (https://github.com/phisher98/cloudstream-extensions-phisher)。
  - ### Cloudstream 的开发者和贡献者们，感谢他们出色的工作，使 Cloudstream 成为 Android 上最佳的可扩展媒体中心之一。
  - ### MustardChef，感谢他提供的 [IPTV 播放列表检查器](https://github.com/MustardChef/IPTVPlaylistChecker) 脚本及工作流程，已改编用于本仓库。
