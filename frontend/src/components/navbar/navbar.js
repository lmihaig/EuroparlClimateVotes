import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  return (
    <header className="">
      <nav className="navbar navbar-expand-lg navbar-light bg-light w-100">
        <div className="navbar-nav d-flex w-100">
          <button
            class="btn btn-primary ms-3"
            onClick={() => {
              navigate("/");
            }}
          >
            Home
          </button>
          <div className="d-flex mx-auto ">
            <button
              className="btn"
              onClick={() => {
                navigate("/MembersOfParliament");
              }}
            >
              Members of the European Parliament
            </button>

            <button
              className="btn"
              onClick={() => {
                navigate("/Laws");
              }}
            >
              Voted laws in the European Parliment
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;
