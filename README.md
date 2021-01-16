# ableton-project-tool
A command line interaction-based python script to organize and manage Ableton Live project files

## Background
When creating music with Ableton Live, a user creates projects which aide in the formation of a song. Each project has a 'project file' containing information ranging from samples and plugins utilized in the project, to the list of tracks making up the song, to the positions of each note or audio clip on each track along the timeline. Once the user has decided they are happy with the song they have created, they can export the song into a single WAV or FLAC audio file.

One of the biggest issues I have identified with this workflow is the lack of connection between a project file and its corresponding finished audio file. Most notably, the project file is usually saved for the first time, and therefore named, very early in the process, long before the song is finished and ready to be exported. Typically, I will name the project according to one of its most defining characteristics, such as `upbeat piano.als` or `melancholy guitar.als`, or worse, the dreaded keyboard smash: `asdfguh;oi.als`. If I want to return to a previously finished song, there's not much I can do to find the old project file aside from guesswork based on the date I last worked on it or the name, providing it was at least somewhat descriptive of how some early stage of the song sounded.

## Project Breakdown
This project is still a work in progress. Once completed, it will perform as such:

The script stores all of my Ableton project files in a JSON file, with additional keys:
  * Whether the project is finished or not
  * The name of the finished song, if it has been finished
  * The names of other artists that this song was been sent to, if any

Upon running of this script from command line, it will automatically recur through the layers of folders in which I store my project files, check to see if any of them have been created since the script's last running, and add any such files to the JSON.

At this point, the script will ask what the user wants to do. The main action the user can take at this point is to update the JSON. For example, say you have completed a project and exported the song. Now you can go back into the script to designate the project you just completed as finished, inputting the name of the exported song, and listing the artists you sent it to, if relevant.

Once the JSON is fully filled in, the user can search it by various filters. The script will then return, for example, the list of projects that have been finished, or all of the songs you have sent to a certain artist.

The biggest issue with the project at this point is its inability to fill in the additional keys automatically, especially upon first running, forcing the user to manually fill in, one by one, the information for however many projects the user was unfortunate enough to create before running the script for the first time. I currently have no ideas about how to fix this rather inconvenient issue with the tool. If you have any thoughts about this or any other aspect of the project, please contact me as I would love to hear them!
