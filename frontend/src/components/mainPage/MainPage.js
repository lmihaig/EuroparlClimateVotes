import React from "react";

function MainPage() {
  return (
    <div>
      <div class="d-flex flex-column min-vh-100 justify-content-center align-items-center">
        <div class="text-center">
          <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="sun bi bi-brightness-high" viewBox="0 0 16 16">
            <path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" />
          </svg>
        </div>

        <h1 class="text-center m-top-10 f-size-60 ">
          Political Climate
        </h1>
        <p class="text-center">
          FIND OUT EVERY POLITICIAN'S VIEW ON THE CLIMATE
        </p>
        <p class="text-center">
          How anchored in the current climate issues<br></br>
          are the politicians you support?
        </p>
        <p class="text-center bold">
          A politician's interest in saving our environment should<br></br>
          be a key factor in choosing who to vote.
        </p>
        <div class="d-flex justify-content-center gap-3" > 
          <a class="research-btn bold" href="/MembersOfParliament">Members of the European Parliment</a>
          <a class="research-btn bold" href="/Laws">Voted laws in the European Parliment</a>
        </div>
        <footer class="site-footer">
          <div class="footer-container">
            <ul class="footer">
            <li><a>About</a></li>
            <li><a>Methodology</a></li>
            <li><a>FAQ</a></li>
            </ul>
          </div>
        </footer>
      
       
      </div>
      
    </div>
  );
}

export default MainPage;
