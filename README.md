# cowsay server

## specification

endpoints
- GET `/cow[?msg=]` returns raw text of cowsay with the optional message
- POST `/cow[?msg=]` returns JSON with "content" key assigned the raw text from a GET

examples
- /cow?msg=text

```
______
< text >
------
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\
          ||----w |
          ||     ||
```
- /cow?msg=Hello user!

```
_____________
< Hello user! >
-------------
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\
          ||----w |
          ||     ||
```
- /cow

```
___________________________________
< You should speak up for yourself. >
-----------------------------------
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\
          ||----w |
          ||     ||
```
