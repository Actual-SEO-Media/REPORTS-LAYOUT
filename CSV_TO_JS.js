inputFile = document.getElementById("file_csv")



inputFile.addEventListener("change", async () => {

    const csvFile = inputFile.files[0]
    const csv_File = await csvFile.text() 
    CLEANER(csv_File)
    
  
  

   
})
