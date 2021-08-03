

function check_Invoice_Type(){
    const previous_Invoice_Choice = document.getElementById("Previous Invoice");
    const new_Invoice_Choice = document.getElementById("New Invoice");
    const new_Invoice_Number = document.getElementById("New Invoice Number")



    if(new_Invoice_Choice.checked === true){
        alert("Invoice number "+ new_Invoice_Number.value + " has been added to the database.")
    }

    else if (previous_Invoice_Choice.checked === true){
        alert("Good to go.")

    }

}