import React from "react";
import Navbar from "../navbar/navbar";

function MainPage() {
  return (
    <div>
      <Navbar />

      <div class="container-nice m-auto">
        <div class="text-center">
          <svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" fill="currentColor" class="bi bi-thermometer-sun m-top-30" viewBox="0 0 16 16">
            <path d="M5 12.5a1.5 1.5 0 1 1-2-1.415V2.5a.5.5 0 0 1 1 0v8.585A1.5 1.5 0 0 1 5 12.5z" />
            <path d="M1 2.5a2.5 2.5 0 0 1 5 0v7.55a3.5 3.5 0 1 1-5 0V2.5zM3.5 1A1.5 1.5 0 0 0 2 2.5v7.987l-.167.15a2.5 2.5 0 1 0 3.333 0L5 10.486V2.5A1.5 1.5 0 0 0 3.5 1zm5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 .5-.5zm4.243 1.757a.5.5 0 0 1 0 .707l-.707.708a.5.5 0 1 1-.708-.708l.708-.707a.5.5 0 0 1 .707 0zM8 5.5a.5.5 0 0 1 .5-.5 3 3 0 1 1 0 6 .5.5 0 0 1 0-1 2 2 0 0 0 0-4 .5.5 0 0 1-.5-.5zM12.5 8a.5.5 0 0 1 .5-.5h1a.5.5 0 1 1 0 1h-1a.5.5 0 0 1-.5-.5zm-1.172 2.828a.5.5 0 0 1 .708 0l.707.708a.5.5 0 0 1-.707.707l-.708-.707a.5.5 0 0 1 0-.708zM8.5 12a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 .5-.5z" />
          </svg>
        </div>

        <h1 class="text-center m-top--40 f-size-60 ">
          Political Climate
        </h1>
        <p class="text-center">
          FIND OUT EVERY POLITICIAN'S VIEW ON THE CLIMATE
        </p>
        <p class="text-center m-top-40">
          How anchored in the current climate issues<br></br>
          are the politicians you support?
        </p>
        <p class="text-center bold">
          A politician's interest in saving our environment should<br></br>
          be a key factor in choosing who to vote.
        </p>
        <div class="text-center m-top-30">
          <a href="/MembersOfParliament"><button class="research-btn bold">View Our Research</button></a>
        </div>
        <ul class="footer">
          <li><a>About</a></li>
          <li><a>Methodology</a></li>
          <li><a>FAQ</a></li>
          <li></li>
        </ul>
      </div>
    </div>
  );
}

export default MainPage;
