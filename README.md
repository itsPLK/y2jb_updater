# Y2JB Updater

A solution for updating Y2JB on PS5.

## Usage (Updating Y2JB)

### - If using Y2JB (remote loader)

1.  Put the update ZIP in one of these places:
    * `USB/y2jb_update.zip`
    * `/data/y2jb_update.zip`
2.  Start Y2JB, send the kernel exploit (e.g., `lapse.js`), and then
3.  Send **`update.js`**.

The script will update the Y2JB files. If successful, it will also delete the `y2jb_update.zip` package.

---

### - If using ps5_y2jb_autoloader

The updater is included in the autoloader (since version v0.2).
*  Put the update ZIP in one of these places:
    * `USB/y2jb_update.zip`
    * `/data/y2jb_update.zip`

The autoloader will automatically apply the update after loading the kernel exploit.

  ## Creating update package
Use included python script.
```
Usage: python3 create_update_package.py <directory_to_zip>
- <directory_to_zip> is the path to the directory containing splash.html and other Y2JB files.
```
This will generate **y2jb_update.zip** file that can be used with the Updater.

## Safety notes
- The updater uses raw syscalls to manage files and directories. **This script is experimental and has not been extensively tested. Use with caution.**
- The updater performs a temporary move of the existing Y2JB directory before installing the new files. This temporary directory is deleted upon successful completion of the update process.
- If extraction or write operations fail, logs and notifications are sent by the script - check the Y2JB log output for details.
- The updater runs after a kernel exploit, and due to the nature of filesystem modifications via raw syscalls, there is a **risk of data loss or corruption (file wiping)** if errors occur. **Use at your own risk.**
