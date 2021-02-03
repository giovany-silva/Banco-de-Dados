const {Client}=require('pg')
const app =require("express")()
const cient =new Client({
	user:"postgres",
	password:"postgres",
	host:"jhow",
	post:5432,
	database:"BD II"
})

 client.connect();

 app.get("/",async(req,res)=>{
	let result={}
        results.rows=[]
 	try{
	const id=req.query.id;
        
        results=await client.query(`select * from profiles where id=${id}`)
	}
        catch(e)
	{
       console.log("Error")
	}
        finally{
	res.setHeader("content-type","application/json")
        res.send(JSON.stringify(results.rows))
	}
 })

