package main

import (
    "fmt"
    "net/http"
    "log"
    "io/ioutil"
    "strconv"
)

func hello(w http.ResponseWriter, req *http.Request) {

    for i := 1; i < 100; i++ {

        resp, err := http.Get("http://pi:8888/pi/"+strconv.Itoa(i))
        if err != nil {
            log.Fatalln(err)
        }

        body, err := ioutil.ReadAll(resp.Body)
        if err != nil {
            log.Fatalln(err)
        }

        log.Println(string(body))
        fmt.Fprintf(w, string(body))
    }
}

func main() {

    http.HandleFunc("/hello", hello)
    http.ListenAndServe(":8090", nil)
}
