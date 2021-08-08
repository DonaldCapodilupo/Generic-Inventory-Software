function check_Invoice_Type(){
    const previous_Invoice_Choice = document.getElementById("Previous Invoice");
    const new_Invoice_Choice = document.getElementById("New Invoice");
    const new_Invoice_Number = document.getElementById("New Invoice Number");



    if(new_Invoice_Choice.checked === true && new_Invoice_Number.value){
        document.getElementById("New Invoice Confirmation Wrapper").style.display = "block";
        document.getElementById("New Contractor Wrapper").style.display = "block";
        document.getElementById("Final Choice Wrapper").style.display = "none";
    }

    else if (new_Invoice_Choice.checked === true && new_Invoice_Number.value === ""){
        alert("You cannot leave the invoice number field blank.");

    }

    else if(previous_Invoice_Choice.checked === true){
        document.getElementById("New Contractor Wrapper").style.display = "none";
        document.getElementById("Final Choice Wrapper").style.display = "block";
    }

}

function verify_Contractor(){
    const previous_Contractor_Choice = document.getElementById("Previous Contractor");
    const new_Contractor_Choice = document.getElementById("New Contractor");
    const new_Contractor_Name = document.getElementById("Contractor Name");



    if(new_Contractor_Choice.checked === true && new_Contractor_Name.value){
        document.getElementById("New Contractor Accepted").style.display = "block";
        document.getElementById("Final Choice Wrapper").style.display = "block";

    }

    else if (new_Contractor_Choice.checked === true && new_Contractor_Name.value === ""){
        alert("You need to fill in the \"New Contractor Name\" field.");

    }

    else if (previous_Contractor_Choice.checked === true){
        document.getElementById("Final Choice Wrapper").style.display = "block";
    }



}