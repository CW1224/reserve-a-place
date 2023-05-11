# Awesome Dishes

Welcome to the readme file of my project.

## Introduction

This programme is designed to allow an user to 

You can find a link to my website [here]()

# Table of Contents
[1.User Experience(UX)](#1-user-experience)
- 1.1 User Goals
- 1.2 User Expectations
- 1.3 Visual Images
- 1.4 Brainstorm

[2.Features](#2-features)
- 2.1 

[3.Technology](#3-technology)

[4.Testing](#4-testing)

[5.Bugs](#5-bugs)

[6.Deployment](#6-deployment)

[7.Project Completion](#7-project-completion)

[8.Improvements](#8-improvements)

[9.Acknowledgements](#9-acknowledgements)

# 1. User Experience

## 1.1 User Goals

[Return to the Table of Contents](#table-of-contents)

My goal in creating this programme 

## 1.2 User Expectations

[Return to the Table of Contents](#table-of-contents)

The following are expected of the website:

* Should be easily accessible.
* The language should be in simple English.
* 

## 1.3 User Stories

[Return to the Table of Contents](#table-of-contents)



## 1.4 Strategy Table

[Return to the Table of Contents](#table-of-contents)

## 1.5 Wireframes

[Return to the Table of Contents](#table-of-contents)



# 2. Features

[Return to the Table of Contents](#table-of-contents)

## 2.1 Navigation Bar

## 2.2 Login, Signup and Logout

## 2.3 Menu, Contacts and Homepage

## 2.4 Making a Booking

## 2.5 Edit a Booking and Deleting a Booking

## 2.6 Manage all bookings

# 3. Technology

[Return to the Table of Contents](#table-of-contents)

* [MD](https://en.wikipedia.org/wiki/Markdown) (Markdown) was used to create this readme file.

* [Gitpod](https://www.gitpod.io/) was used for the code input and edit for this project.

* [Github](https://github.com/) was used to store my repository and code when it is not in use.

* [Slack](https://slack.com/intl/en-ie/) was used for communications when I was having trouble creating code.

* [Pep8 Validator](http://pep8online.com/) was used to check for bugs in my code.

* [Heroku](https://id.heroku.com/login) was used to deploy my project.

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used to create the website.

* [JS](https://en.wikipedia.org/wiki/JavaScript)(JavaScript) was used to make the website.

* [HTML5](https://en.wikipedia.org/wiki/HTML5) (Hypertext Markup Language 5) was used to create the webpages.

* [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) was used to style the webpages.

* [PostgreSQL](https://www.postgresql.org/) was used as a database.

* [Pixabay](https://pixabay.com/) was used to download images. These images were then uploaded onto Cloudinary.

* [Cloudinary](https://cloudinary.com/) was used as a database to store images.

* [Google Fonts](https://fonts.google.com/) was used to import the font style for my project.

# 4. Testing

[Return to the Table of Contents](#table-of-contents)

The contents of the testing section can be find [here](testing.md).

# 5. Bugs

[Return to the Table of Contents](#table-of-contents)


# 6. Deployment

[Return to the Table of Contents](#table-of-contents)

The site was deployed to Heroku using the following steps:

2. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

# 7. Project Completion

[Return to the Table of Contents](#table-of-contents)


# 8. Improvements

[Return to the Table of Contents](#table-of-contents)


# 9. Acknowledgements

[Return to the Table of Contents](#table-of-contents)

* Credits is given to [iKelvv](https://github.com/iKelvvv/MS4) for given me some code to be used in the programme. This is the code that was implemented into my programme in which I modified.
```
class EditBooking(View):
    model = Booking
    template_name = 'edit_booking.html'
    context_object_name = 'edit_booking'

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                "updated": False,
                "Update_Booking": UpdateBooking(instance=booking)
            },
        )

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)

        booking_details_form = UpdateBooking(
            request.POST, instance=booking)

        if booking_details_form.is_valid():
            booking.status = 0
            booking_updates = booking_details_form.save()
        else:
            booking_details_form = UpdateBooking(instance=booking)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                'updated': True,
                "Update_Booking": booking_details_form,
            },
        )
``` 
```
class DeleteBooking(DeleteView):
    model = Booking
    pk_url_kwarg = "booking_id"
    success_url = reverse_lazy("reservations")
    template_name = "delete_booking.html"
```
```

```
```

```
```

```
* Credits is given to the Codestar walkthrough tutorial for 
```
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-created_date')
    template_name = 'reservations.html'
    paginate_by = 6
    extra_context = {
        "view_booking_active": "pressed"
    }

    def get_queryset(self):
        return Booking.objects.filter(user_id=self.request.user)
```
* For the Readme file, I took the structure from my previous Readme file and used it here. Reference is given to https://github.com/dhakal79/Portfolio-project-MS1 which is the readme file I took into consideration when I was doing my first one.

* The ideas and code I implemented into this project were taught to me by Code Institute.
* My mentor Marcel Mulders supported me throughout the whole project. I couldn't have done it without his help.