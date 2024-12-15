// 引入默认实例
import { marked } from 'marked'

import { markedHighlight } from "marked-highlight"
import hljs from 'highlight.js'
// 注意引入样式，你可以前往 node_module 下查看更多的样式主题
import 'highlight.js/styles/base16/darcula.css'


// 高亮拓展
marked.use(markedHighlight({
  langPrefix: 'hljs language-',
  highlight(code, lang) {
    const language = hljs.getLanguage(lang) ? lang : 'shell'
    return hljs.highlight(code, { language }).value
  }
}))

marked.use({
  // 开启异步渲染
  async: true,
  pedantic: false,
  gfm: true,
  mangle: false,
  headerIds: false
})

// 异步方式渲染
marked.parse(markdown, { async: true }).then((html: string) => {
	console.log(html)
})

// 同步方式渲染
const html = marked.parse(markdown)
