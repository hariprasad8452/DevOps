# --- THE ULTIMATE LINUX COMMAND CENTER (linux.py) ---

# --- 1. SYSTEM INFORMATION (Know your machine) ---
# uname            -> See OS type
# uname -r         -> See kernel version
# uname -a         -> Full system info (Kernel, OS, Arch)
# hostname         -> See current machine name
# hostnamectl set-hostname harry -> Change hostname to 'harry'
# hostname -i      -> See IP address (also: ifconfig, ip addr, ip addr show)
# cat /proc/cpuinfo -> Detailed CPU info (also: lscpu)
# cat /proc/meminfo -> Detailed memory info (also: lsmem)
# cat /etc/os-release -> See Linux distribution details (also: cat /proc/version)

# --- 2. FILE & DIRECTORY OPERATIONS ---
# touch file1      -> Create an empty file
# touch {1..5}     -> Create multiple files at once (1, 2, 3, 4, 5)
# ls               -> List filenames only
# ll               -> Long list (shows permissions, owner, size, date)
# ls -a            -> Show hidden files (those starting with a dot .)
# mkdir d1         -> Create a directory
# mkdir -p d1/d2   -> Create nested directories (parent and child)
# cp f1 f2         -> Copy f1 to f2
# mv f1 f3         -> Rename f1 to f3 (content remains same)
# rm -f file1      -> Force delete a file
# rm -rf * -> DANGER: Delete EVERYTHING in current folder

# --- 3. READING & WRITING CONTENT ---
# cat file1        -> Print entire content of file1
# more file1       -> View content page by page
# cat > file1      -> INSERT content (Overwrites existing data)
# cat >> file1     -> APPEND content (Adds to the end of file)
# cat >> b a       -> Copy data from file 'a' into 'b' without overwriting 'b'
# head -15 file1   -> See top 15 lines
# tail -15 file1   -> See bottom 15 lines
# %s/old/new       -> (Inside Vim) Global search and replace in a file

# --- 4. PERMISSIONS & OWNERSHIP (The 4-2-1 Rule) ---
# Structure: - rwx r-- r-- (1=ACL, root=Owner, root=Group, 0=Chars)
# r (Read) = 4 | w (Write) = 2 | x (Execute) = 1
# Example: chmod 764 file1
# 7 (4+2+1) -> User can Read/Write/Execute
# 6 (4+2)   -> Group can Read/Write
# 4 (4)     -> Others can only Read

# chmod 762 file1  -> U=7(rwx), G=6(rw-), O=2(-w-)
# chown hari file1 -> Change owner to 'hari'
# chgrp hari file1 -> Change group to 'hari'
# chown hari:hari file1 -> Change both owner and group in one step

# --- 5. USER & GROUP MANAGEMENT ---
# useradd harry    -> Create a new user
# userdel harry    -> Delete a user
# id harry         -> See UID, GID, and groups for user 'harry'
# w                -> See who is logged in and what they are doing
# whoami           -> See your current active username
# cat /etc/passwd  -> List all users (also: getent passwd)
# cat /etc/group   -> List all groups (also: getent group)

# --- 6. RESOURCE MONITORING ---
# free -m          -> See RAM usage in MB (Used vs Free)
# lsblk            -> List block devices (Hard drives/EBS volumes)
# df -h            -> Disk space usage in human-readable format (GB/MB)
# top              -> Real-time process monitor (Task Manager)

# --- THE LINUX GOLDEN RULES ---
# 1. ROOT IS GOD: Commands starting with 'sudo' have total power.
# 2. PATHS: '/' is root directory, '~' is your home directory.
# 3. APPENDING: Always check if you need '>' (overwrite) or '>>' (append).
# 4. HELP: Use 'man <command>' if you forget how a command works.

print("Linux Environment: Ready.")
print("Harry, your custom hostname and user commands are loaded.")
print("Remember: Permissions 755 is standard for folders, 644 for files.")
