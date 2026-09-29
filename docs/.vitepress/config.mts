import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: '在想法与实现之间',
  description: '从人的视角理解 AI 协作开发',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '写在前面', link: '/start/' },
      { text: '文档地图', link: '/document-map/' },
      { text: '机制原理', link: '/mechanism/' }
    ],
    sidebar: {
      '/start/': [
        {
          text: '写在前面',
          items: [
            { text: '脑中的那张地图', link: '/start/' }
          ]
        }
      ],
      '/document-map/': [
        {
          text: '项目 docs/ 目录',
          items: [
            { text: '目录总览', link: '/document-map/' },
            { text: 'requirements/ · 需求', link: '/document-map/requirements' },
            { text: 'design/ · 体验设计', link: '/document-map/design' },
            { text: 'architecture/ · 技术架构', link: '/document-map/architecture' },
            { text: 'dev/ · 合同与任务', link: '/document-map/dev' },
            { text: 'reports/ · 检查与验收', link: '/document-map/reports' },
            { text: 'control/ · 运行定义', link: '/document-map/control' },
            { text: 'rules/ · 工程规则', link: '/document-map/rules' },
            { text: 'guides/ · 使用说明', link: '/document-map/guides' },
            { text: 'examples/ · 合成示例', link: '/document-map/examples' }
          ]
        }
      ],
      '/mechanism/': [
        {
          text: '机制原理',
          items: [
            { text: '一项 REQ 的阶段地图', link: '/mechanism/' },
            { text: 'S0～S2 · 意图与设计', link: '/mechanism/intent' },
            { text: 'S3～S5 · 契约与计划', link: '/mechanism/plan' },
            { text: 'S6～S7 · 构建与验证', link: '/mechanism/build-and-check' },
            { text: 'S8～S9 · 调查与修复', link: '/mechanism/investigate-and-repair' },
            { text: 'S10～S11 · 验收与决定', link: '/mechanism/release' },
            { text: '辅助：三份不同的记录', link: '/mechanism/req-identity' }
          ]
        }
      ]
    },
    outline: { label: '本页内容' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '外观',
    lastUpdatedText: '更新于'
  }
})
