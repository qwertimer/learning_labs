# Notes

* The `println` function is built in to Go and is printed to `STDERR`.
* We can use `go run .` to run main.go and have foo.go work implicitly
* `go install` installs to a system path.
* `go test` does reflection and looks into the code in the folder. We
  show expected output with comments by writing for example

  `` 
  func ExampleFoo() {
  //Output:
  //foo-go
  }``
  and run `go test`
* We can then run autotesting with entr
  `` entr bash -c "clear; go run ." < <(find .)``

