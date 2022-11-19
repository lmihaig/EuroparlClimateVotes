import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  return (
    <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="#" onClick={() => {
          navigate("/");
        }}>
                Home <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item active">
              <a
                class="nav-link"
                href="#"
                onClick={() => {
                  navigate("/MembersOfParliament");
                }}
              >
                Parlamentari <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item active">
              <a
                class="nav-link"
                href="#"
                onClick={() => {
                  navigate("/Laws");
                }}
              >
                Legi
              </a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;
