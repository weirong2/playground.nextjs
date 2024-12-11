## Dev
#### Launch
```
pnpm dev
```
or
```
cd nextjs-dashboard
pnpm run dev
```

## Issues

#### install pnpm permission denied
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

#### set application port (default is 3000) to a different number
change package.json from
```
    "dev": "next dev --turbo",
```
to
```
    "dev": "next dev --turbo -p 4000",
```
