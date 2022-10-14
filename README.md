# HealthSimple
https://devpost.com/software/healthsimple-hlp28w

### Inspiration
Since the beginning of the COVID-19 pandemic, WFH and online school has fatigued us all. As remote learners ourselves, our team wanted to create a hack that could help digital workers and students improve mental and physical health. While brainstorming for solutions, our team realized that we often forget to take breaks from staring at our screens and sitting for prolonged periods of time. We also identified "Zoom fatigue" as a common problem among remote workers and students. As such, we decided to create a wellness widget for desktops.

### What it does
HealthSimple is a desktop widget that delivers motivation messages, as well as reminders for hydration and physical activity. Users have the option to select which category of messages they would like to receive (ie: motivation, hydration, activity). They can also decide the time intervals at which messages are delivered. For example, if you wish to be reminded to take breaks from your desk every half hour, you would select "activity" as your category and enter "30" as your time interval. HealthSimple will then deliver an activity message, which can range from a posture reminder to an exercise suggestion, every 30 minutes.

### How we built it
Our team used Python as our programming language. Within Python, we used the Plyer library to access the features of the hardware and because it is platform-independent. For the GUI, we used the Tkinter and PIL libraries.

### Challenges we ran into
The main challenge that we ran into was trying to ensure that while the notifications ran in the background, the user would still be able to interact with the main GUI. To do this, our team learned the differences between threading and multiprocessing, both of which allow for different parts of the program run concurrently. We eventually decided to use threading because multiprocessing uses different memory space while threading uses the same. Figuring out how to run notifications while also keeping the main GUI interactive and then learning how to implement threading in Python was challenging.

### Accomplishments that we're proud of
Our team met each other only on the first day of the hackathon. We're proud that we were able to collaborate effectively in a virtual environment despite having had no experience working together before. Most of us were also hackathon newbies yet we were still able to complete our hack and pitch in less than 36 hours!

### What's next for HealthSimple
There are several other features that HealthSimple is hoping to implement, including a Pomodoro timer. As WFH becomes increasingly prevalent, it's important that the modern worker is equipped with tools that keep them happy, healthy, and productive. We would also love to test HealthSimple with prospective users, and iterate on their feedback to improve user flow, functionality, and product design.
