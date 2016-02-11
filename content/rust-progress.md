Title: Learning Rust
Date: 2015-12-02
Modified: 2015-12-02
Category: Learning
Authors: Kenneth Lyons
Summary: My progress in learning about the Rust language
Status: draft


Over the long Thanksgiving weekend, I struck up an interest in [Rust].
I started out reading through [the book][rust book], but I switched over to
[Rust by Example], which I plan to work all the way through. This post just
contains some of my thoughts as I learn a new programming language for the
first time in quite a while.


# It's Like Python!

I was immediately struck by a few clear points of influence from Python. For
example, the string formatting:

```rust
println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
```

Also, for loops:

```rust
for item in vec.into_iter() {
    println!("{:?}", a);
}
```


# Steep Learning Curve

Although I never really got far in learning Haskell, learning Rust feels in
some ways very similar. If I had to pinpoint what exactly it is that's similar,
I'd say it's how much of the language you have to understand to even write
simple programs. That's kind of given with Haskell, but Rust is *kind of*
C-like, so you expect to get up and running with it a bit more quickly.

Python has this sort of split between use cases: scripts and full programs. You
can get by writing scripts in Python (e.g. for data analysis) without
understanding really anything about Python itself (how it handles memory, for
example). You can actually get by writing fairly sophisticated programs in
Python without really knowing what's going on. In Rust, this is definitely not
the case -- you have to have an understanding of *ownership* and *lifetimes*
before you start writing any code at all. If you don't, have fun fighting the
compiler. It is the care with which you have to think through what you want to
do before you do it that reminds me of my extremely limited experience with
Haskell.


# Building and Packaging

I have to say I'm completely impressed with `rustc` and `Cargo`. Rust is
a modern language, and that is probably most apparent here.


[rust book]: https://doc.rust-lang.org/stable/book/
[Rust]: https://www.rust-lang.org/
[Rust by Example]: http://rustbyexample.com/
