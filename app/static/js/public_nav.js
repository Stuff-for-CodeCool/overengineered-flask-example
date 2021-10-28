//  This needs to be wrapped in a function, to ensure the links are correctly read each time
const processLinks = () => {
    //  Get all links on page
    document.querySelectorAll("main nav a").forEach((a) =>
        //  Add a click listener
        //  Notice the handler is an async function
        a.addEventListener("click", async (e) => {
            //  Prevent click action
            e.preventDefault();
            //  Fetch the content of the linked page
            const req = await fetch(e.target.href, {
                //  Force the fetch to be a JSON request
                headers: { "Content-Type": "application/json" },
            });
            //  If the request succeeded
            if (req.ok) {
                //  Convert the response to JSON
                const res = await req.json();
                //  Inject the fetched content into the document
                document.querySelector("main").innerHTML = res.message;
                //  After the content is regenerated, ensure the links are read again
                processLinks();
            }
        })
    );
};

processLinks();
