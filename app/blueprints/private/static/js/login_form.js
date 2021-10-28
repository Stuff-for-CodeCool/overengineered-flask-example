//  Define a function handling login forms
const loginForm = () => {
    //  Get the form
    document
        .querySelector("form")
        //  Listen to the "submit" event
        .addEventListener("submit", async (e) => {
            //  Send the data
            //  The form's action URL is the fetched URL 
            const req = await fetch(e.target.action, {
                //  The form's method is the fetch method
                method: e.target.method,
                //  Set it as a JSON request
                headers: { "Content-Type": "application/json" },
                //  For POSTs, you need to specify a body
                //  which will be a JSON string of an object;
                //  keys are what the server expects, values are fields' names' values
                body: JSON.stringify({
                    username: e.target.username.value,
                    password: e.target.password.value,
                }),
            });
            //  Request succeeded
            if (req.ok) {
                //  Convert response into JSON
                const res = await req.json();
                //  Inject JSON data
                document.querySelector("main").innerHTML = res.message;
            }
        });
};

loginForm();
