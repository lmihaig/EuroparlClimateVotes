function MPPage() {
    return (
        <div>
            <div class="mpp-header m-top-20">
                <div class="container m-auto">
                    <div class="filter-sort">
                        <img src="images/filter-icon.svg" alt="" width="25" height="25"></img>
                        <img src="images/sort-icon.svg" alt="" width="25" height="25"></img>
                    </div>
                    <div class="search-bar">
                        <img src="images/search-icon.svg" alt="" width="25" height="25"></img>
                        <p class="search-text">Search</p>
                    </div>
                </div>
            </div>

            <div class="mpp-list m-top-40">

                <div class="list-politician">
                    <img class="politician-img margin-red" src="images/obama.webp"></img>
                    <div class="politician-info">
                        <p class="politician-name m-top-5">Obma</p>
                        <p class="politician-descr">my president</p>
                    </div>
                </div>
                <div class="list-politician">
                    <img class="politician-img margin-yellow" src="images/obama.webp"></img>
                    <div class="politician-info">
                        <p class="politician-name m-top-5">Obma</p>
                        <p class="politician-descr">my president</p>
                    </div>
                </div>
                <div class="list-politician">
                    <img class="politician-img margin-green" src="images/obama.webp"></img>
                    <div class="politician-info">
                        <p class="politician-name m-top-5">Obma</p>
                        <p class="politician-descr">my president</p>
                    </div>
                </div>
                <div class="list-politician">
                    <img class="politician-img margin-yellow" src="images/obama.webp"></img>
                    <div class="politician-info">
                        <p class="politician-name m-top-5">Obma</p>
                        <p class="politician-descr">my president</p>
                    </div>
                </div>
        
            </div>
        </div>
    );
}

export default MPPage;