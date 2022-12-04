package main

import (
    "fmt"
    "log"
    "os"
    "net/http"
)

func network(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/" {
        http.Error(w, "404 not found.", http.StatusNotFound)
        return
    }

    switch r.Method {
    case "GET":
      db, err := os.ReadFile("db.json")
      if err != nil {
          http.Error(w, "Error open file", http.StatusNotFound)
          return
      }else {
        fmt.Fprintf(w, string(db))
      }
    case "POST":
        // Call ParseForm() to parse the raw query and update r.PostForm and r.Form.
        if err := r.ParseForm(); err != nil {
            fmt.Fprintf(w, "ParseForm() err: %v", err)
            return
        }
        name := r.FormValue("user")
        msg := r.FormValue("msg")
        os.WriteFile("db.json", []byte("{\"user\":\""+name+"\",\"msg\":\""+msg+"\"}"), 0644)
        fmt.Fprintf(w, "POST correct")
    default:
        fmt.Fprintf(w, "Sorry, only GET and POST methods are supported.")
    }
}

func main() {
    http.HandleFunc("/", network)

    fmt.Printf("Starting server for testing HTTP POST...\n")
    if err := http.ListenAndServe("192.168.0.188",":3000", nil); err != nil {
        log.Fatal(err)
    }
}
