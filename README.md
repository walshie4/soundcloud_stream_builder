#Soundcloud Stream Builder

A Python helper to get the contents of a user's stream. ([or close to it](#known-issues)))

---

###Known Issues

As explained [here](//stackoverflow.com/a/14925854) the SoundCloud API does not
yet expose user's reposts so reposts are not included in the user's stream. This
makes this script return the newest songs (within the age timeout) posted by
users followed by the current authorized user.

---

###License

MIT - see `LICENSE`

