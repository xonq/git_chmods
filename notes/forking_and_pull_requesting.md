How Setup a Forked Repo
-------
1. Log into [GitHub](http://github.com) with your user name (create an account if you don't already have one).

2. Next, go to the [*git_chmods* repo](https://github.com/xonq/git_chmods) and
click on the "Fork" button in the upper-right corner ofthe page (under your
profile picture/avatar). This will create for you your own remote copy of the
*git_chmods* repo.

3. After forking, you'll be taken to your newly-forked repo. Next, click on the green "Clone or download" button and make sure "Clone with HTTPS" is selected. Copy the URL provided.

4. In the Terminal application, clone your remote repository (origin) to your (local) computer:
   ```bash
   git clone paste-your-url-here
   ```

5. Next, link the `xonq/git_chmods` remote repo URL as your local repo's "upstream" remote repository:
   ```bash
   cd git_chmods
   git remote add upstream https://github.com/xonq/git_chmods.git
   ```

For a more in-depth tutorial on forking, please visit the [GitHub Help](https://help.github.com/en/articles/fork-a-repo) page.


How To Sync
-------

[Link to online GitHub Instructions](https://help.github.com/en/articles/syncing-a-fork)

Now that your forked repo is cloned and configured with "upstream", you have a three-node directed-graph of remote and local repositories. The graph is directed because changes will flow in only one direction, as shown in the following diagram:
```
     [upstream/git_chmods] <-- [origin/git_chmods]
              |                  ^
	      V                  |
             [local/git_chmods] ----+
```

You may now add changes to your local repo. To do this, follow these steps:

1. Pull down to your local repo any changes that other contributors may have synced with the upstream remote repo:
   **NOTE: It is very important that you do this *every* time you want to `add`/`commit`/`push` changes to your local repo** 

2. Make your changes to the necessary file(s).

3. `add` and `commit` your changes to your local repo:
   ```bash
   git add path-to-modified-files
   git commit -m 'Add descriptive message, summarizing changes'
   ```

4. Then `push` those changes to your remote repo:
   ```bash
   git push origin main
   ```

5. In your browser, go to your forked remote repo page on [GitHub](http://github.com), click the "Pull requests" tab (under repo name), and click on the blue "create a pull request" link under the "Welcome to Pull Requests!" banner.

6. You'll be presented with a form page, fill in the pull request title and provide a description summarizing the changes you've made.

7. Click the green "Create Pull Request" button to submit the pull request.

For a more in-depth tutorial on creating pull requests, please visit the [GitHub Help](https://help.github.com/en/articles/creating-a-pull-request) page.

