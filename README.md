# Mother of Automations
 Congrats on your interest in this repo :)
 
 ## Git Guide lines
 
 1. First of all, all the new projects or changes to an existing code should be done on a seperate branch. Say you are building a project "wallpaper-changer", then name your branch to "<your_name>-wallpaper-changer" . Why? It makes tracking of every change easy.
 
 2. Once you are done with all the required changes in your project, create a pull request for that branch. **Do not push to master**
 
 3. Do ***NOT*** merge any branch with any other branch. Always use *git rebase*.
    Say you are on branch *jibin-temp* which you have created 10 days back. Now till date there were some other pushes in master branch due to which your branch has diverted from master. To incoorporate the master branch code in your branch, do the following in your local repository.
    
    ```shell
      $ git add .
      $ git commit -m "<Commit message>"
      $ git checkout master
      $ git pull origin master
      $ git checkout jibin-temp
      $ git rebase master
      $ git push origin jibin-temp -f
    ```
    If any rebase conflicts occur, resolve them and do ``` $ git rebase --continue ```  till all your conflicts are resolved.
    Once you rebase you branch with master you might need to force push your branch.
 
 4. **Never. Never Ever** force push to master. If you have to force push, do it on your branch. Do not screw up the master branch.
 
 5. If more than one of you are editing the same file, try to avoid editing on the same line numbers. Say one of you is editing on line 20, others avoid adding or removing anything on line 20. There is no problem with this but this *might* lead to conflicts.
 
 6. Once you are done with changes and created a pull request, Assign that pull request to some other developer. Review your code from some other developer atleast once. You might learn a new thing or two.
 
 7. For new projects, always update the Readme.md file in that project's root directory. Don't keep anyone guessing what this directory is about.
 
 8. **Administrators** - When you merge any pull request, avoid "Create a merge commit" it with master. Instead use "Rebase and Merge" to merge the changes to master.
 
 9. Whenever a new project is completed and pushed to master, create a new branch named "REL-<date>" say "REL-2017-07-31" or "REL-<project_name>" from the master branch and keep it aside. Do not make any changes to this branch once it is created. This way you have a backup of your previous checkpoint if you screw up master branch.
 
 10. Keep all logical changes in different commits. If there are too many commits, then use git squash .
 
 ## Code Guidelines
 
 1. You are an awesome developer. But not everyone contributing has the same level of awesomeness. So what you write may not be understandable to other. Try to maintain a uniform coding style throught the repository and for that use:
    - Code linters
    - Prettifiers
Every language has such tools. Use them.

2. While code reviewing other's code, look for unoptimised coding patterns, bad coding practices.

3. Use the IDE of your choice but maintain the code styling.

***Cheers***   
**Enjoy the code   
Love what you do   
Do what you love**  
