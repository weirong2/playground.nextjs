# Dev
```
cd nextjs-dashboard
```
## Launch
```
pnpm dev
```
or
```
pnpm run dev
```

# Issues
## install pnpm permission denied
```
» npm install -g pnpm
npm error code EACCES
npm error syscall mkdir
npm error path /usr/local/lib/node_modules/pnpm
npm error errno -13
npm error Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules/pnpm'
npm error     at async mkdir (node:internal/fs/promises:857:10)
npm error     at async /usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:624:20
npm error     at async Promise.allSettled (index 0)
npm error     at async [reifyPackages] (/usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:325:11)
npm error     at async Arborist.reify (/usr/local/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:142:5)
npm error     at async Install.exec (/usr/local/lib/node_modules/npm/lib/commands/install.js:150:5)
npm error     at async Npm.exec (/usr/local/lib/node_modules/npm/lib/npm.js:207:9)
npm error     at async module.exports (/usr/local/lib/node_modules/npm/lib/cli/entry.js:74:5) {
npm error   errno: -13,
npm error   code: 'EACCES',
npm error   syscall: 'mkdir',
npm error   path: '/usr/local/lib/node_modules/pnpm'
npm error }
npm error
npm error The operation was rejected by your operating system.
npm error It is likely you do not have the permissions to access this file as the current user
npm error
npm error If you believe this might be a permissions issue, please double-check the
npm error permissions of the file and its containing directories, or try running
npm error the command again as root/Administrator.
npm error A complete log of this run can be found in: /Users/weirong/.npm/_logs/2024-12-05T01_41_38_728Z-debug-0.log
``` 
```
sudo npm install -g pnpm
```
or [How do I fix the npm error EACCES: permission denied?](https://stackoverflow.com/questions/69421649/how-do-i-fix-the-npm-error-eacces-permission-denied)

## set application port (default is 3000) to a different number
change package.json from
```
    "dev": "next dev --turbo",
```
to
```
    "dev": "next dev --turbo -p 4000",
```

## CanaryOnlyError: The experimental feature "experimental.ppr" can only be enabled when using the latest canary version of Next.js.
```
» pnpm run dev

> @ dev /Users/weirong/Documents/repos/gl/pub/playground.nextjs/001_learn/nextjs-dashboard
> next dev --turbo -p 4000

/Users/weirong/Documents/repos/gl/pub/playground.nextjs/001_learn/nextjs-dashboard/node_modules/.pnpm/next@15.0.3_react-dom@19.0.0-rc-cd22717c-20241013_react@19.0.0-rc-cd22717c-20241013__react@19.0.0-rc-cd22717c-20241013/node_modules/next/dist/server/config.js:241
            throw new CanaryOnlyError('experimental.ppr');
                  ^

CanaryOnlyError: The experimental feature "experimental.ppr" can only be enabled when using the latest canary version of Next.js.
    at assignDefaults (/Users/weirong/Documents/repos/gl/pub/playground.nextjs/001_learn/nextjs-dashboard/node_modules/.pnpm/next@15.0.3_react-dom@19.0.0-rc-cd22717c-20241013_react@19.0.0-rc-cd22717c-20241013__react@19.0.0-rc-cd22717c-20241013/node_modules/next/dist/server/config.js:241:19)
    at loadConfig (/Users/weirong/Documents/repos/gl/pub/playground.nextjs/001_learn/nextjs-dashboard/node_modules/.pnpm/next@15.0.3_react-dom@19.0.0-rc-cd22717c-20241013_react@19.0.0-rc-cd22717c-20241013__react@19.0.0-rc-cd22717c-20241013/node_modules/next/dist/server/config.js:843:32)
    at async Module.nextDev (/Users/weirong/Documents/repos/gl/pub/playground.nextjs/001_learn/nextjs-dashboard/node_modules/.pnpm/next@15.0.3_react-dom@19.0.0-rc-cd22717c-20241013_react@19.0.0-rc-cd22717c-20241013__react@19.0.0-rc-cd22717c-20241013/node_modules/next/dist/cli/next-dev.js:190:14)

Node.js v20.11.1
 ELIFECYCLE  Command failed with exit code 1.
```
- [stackoverflow](https://stackoverflow.com/questions/79222268/canaryonlyerror-the-experimental-feature-experimental-ppr-can-only-be-enabled)
```
» pnpm i next@canary

   ╭──────────────────────────────────────────────────────────────────╮
   │                                                                  │
   │                Update available! 9.14.4 → 9.15.0.                │
   │   Changelog: https://github.com/pnpm/pnpm/releases/tag/v9.15.0   │
   │                Run "pnpm add -g pnpm" to update.                 │
   │                                                                  │
   ╰──────────────────────────────────────────────────────────────────╯

Downloading next@15.1.1-canary.6: 25.37 MB/25.37 MB, done
 WARN  6 deprecated subdependencies found: are-we-there-yet@2.0.0, gauge@3.0.2, glob@7.2.3, inflight@1.0.6, npmlog@5.0.1, rimraf@3.0.2
Packages: +5
+++++
Progress: resolved 252, reused 224, downloaded 4, added 5, done
Downloading @next/swc-darwin-arm64@15.1.1-canary.6: 41.66 MB/41.66 MB, done

dependencies:
- next 15.0.3
+ next 15.1.1-canary.6

Done in 22.9s
```