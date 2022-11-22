# EuroparlClimateVotes

This project was built within 24h by the team **Augusteam** for the **DevHacks 2022 Climate Change** hackathon sponsored by **Systematic** and it won the **third place** worth 500€.

The app

Microservice makes requests daily to the europarl site and parses the XML files to get the newest voting results.
The ML part uses a LinearSVC to binary classify law titles (climate change related or not) trained on a dataset we labeled ourselves.
Backend in Flask using flask_restx.
Frontend built with React.
