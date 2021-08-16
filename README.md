# miro-images-browser

## Development

If you want to work on a development version, clone this repo and install dependencies:

```console
$ git clone https://github.com/wellcomecollection/miro-images-browser.git
$ cd miro-images-browser
$ pip3 install -r requirements.txt
```

Then start the server:

```console
$ python3 server.py
```

This will start a debug version of the ingest inspector at <http://localhost:6737>.
Any changes made to the app will be reflected immediately in the running version.

To deploy a new version to Glitch, commit your changes and push a commit to the primary branch on GitHub.
It will be automatically pushed to Glitch using GitHub Actions (based on a [blog post by Melissa McEwen](https://dev.to/glitch/automating-my-deploys-from-github-to-glitch-2fpd)).

Note: our post-receive Git hook differs from that in the blog post; we run

```shell
#!/bin/bash
unset GIT_INDEX_FILE
git --work-tree=/app  --git-dir=/app/.git checkout -f
refresh
```

to trigger [an immediate refresh](https://support.glitch.com/t/restarting-the-project-using-consoles-refresh-command-spawns-another-instance-of-the-project/16987), even if the app is already running.
