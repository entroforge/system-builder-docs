# 在想法与实现之间

面向项目负责人的 AI 协作开发指南，使用 VitePress 构建。

## 本地阅读与编辑

使用 Node.js 24，安装依赖后启动：

```sh
npm ci
npm run docs:dev
```

正文位于 `docs/`，导航配置位于 `docs/.vitepress/config.mts`。

## 发布到 GitHub Pages

1. 在仓库 **Settings → Pages → Build and deployment → Source** 中选择 **GitHub Actions**。
2. 将配置和文档提交并推送到 `main`。
3. 在 **Actions** 中查看 `Deploy documentation to GitHub Pages`，等待构建与部署完成。

发布后的地址为 [entroforge.github.io/system-builder-docs](https://entroforge.github.io/system-builder-docs/)。之后每次推送到 `main` 都会重新部署，也可以从 Actions 手动启动。

workflow 使用 GitHub 提供的 Pages 元数据设置站点路径，并用默认 `GITHUB_TOKEN` 部署，无需另设密钥。发布产物来自 `docs/.vitepress/dist/`；构建结果、缓存和依赖由 `.gitignore` 排除。

## 本地检查发布路径

默认本地站点使用 `/`。模拟 Pages 的子路径时，构建与预览使用同一个路径：

```sh
VITEPRESS_BASE=/system-builder-docs/ npm run docs:build
VITEPRESS_BASE=/system-builder-docs/ npm run docs:preview
```

预览地址为 `http://localhost:4173/system-builder-docs/`。如需根路径构建，直接运行 `npm run docs:build`。

部署方式参考 [VitePress 官方部署指南](https://vitepress.dev/guide/deploy#github-pages)。
