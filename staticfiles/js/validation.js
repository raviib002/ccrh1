$( document ).ready(function() {
    /******* Common Email Format Validation - Starts here *********/
    jQuery.validator.addMethod("email", function(value, element) {
      // allow any non-whitespace characters as the host part
      return this.optional( element ) || /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/.test( value );
    }, 'Please enter a valid email address.');
    jQuery.validator.addMethod("emailvalidator", function(value, element) {
      // allow any non-whitespace characters as the host part
      return this.optional( element ) || /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/.test( value );
    }, 'Please enter a valid email address.');
    
    /******* Common Email Format Validation - Ends here *********/
    
    /******* Common Password Validation - Starts here *********/
   $.validator.addMethod("new_password1", function(value) {
      return /^[a-zA-Z0-9!@#$%^&*()_=\[\]{};':"\\|,.<>\/?+-]+$/.test(value)
       && /[a-z]/.test(value) // has a lowercase letter
       && /[A-Z]/.test(value) // has a capitalcase letter
       && /\d/.test(value)//has a digit
       && /[!@#$%^&*()_=\[\]{};':"\\|,.<>\/?+-]/.test(value)// has a special character
      },"must consist  lowercase ,capitalcase letter, number and special characters");
     /******* Common Password Validation - Ends here *********/

// validation for Login Page starts here
    validator = $("#logn_form").validate({
        rules: {
            username: {
                required: true,
                emailvalidator: true,
            },
            password: {
                 required: true,
             },
        },
        messages: {
            username: {
                required: "Email is required"
            },
            password: {
                required: "Password is required",
            },
        },
    });
// validation for Login Page ends here


// validation for change Password starts here
    validator = $("#chang_pswd").validate({
        rules: {
            old_password: {
                required: true,
            },
             new_password1: {
                 required: true,
                 minlength: 8
             },
            new_password2: {
                required: true,
                equalTo : '#newpassword1'
            },
        },
        messages: {
            old_password: {
                required: "Old Password is required"
            },
             new_password1: {
                 required: "New Password is required",
                 minlength: "Password should be atleast 8 characters",
             },
            new_password2: {
                required: "Confirm Password is required",
                equalTo : "Confirm Password should be same as New Password."
            },
        },
    });
// validation for change Password ends here

//validation for Reset password starts here
    validator = $("#reset_psw").validate({
        rules: {
             new_password1: {
                required: true,
                minlength: 8,
                new_password1 : true,
             },
            new_password2: {
                required: true,
                equalTo : '#newpassword1'
            },
        },
        messages: {
             new_password1: {
                 required: "New Password is required",
                 minlength: "Password should be atleast 8 characters",
             },
            new_password2: {
                required: "Confirm Password is required",
                equalTo : "Should be the same as change password."
            },
        },
    });
//validation for change  Reset password  ends here

// validation for forgot Password starts here
    validator = $("#forgt_pswd_form").validate({
        rules: {
            email: {
                required: true,
                emailvalidator: true,
            },
        },
        messages: {
            email: {
                required: "Email is required",
            },
        },
    });
// validation for forgot Password ends here

// validation for forgot Password starts here
    validator = $("#profile_info").validate({
        rules: {
            first_name: {
                required: true,
            },
             mobile_number: {
                digits: true,
                minlength: 10,
                maxlength: 10,
                required: true,
                
            },
            email: {
                required: true,
                email: true,
            },
            pincode : {
                required : false,
                maxlength: 6,
                digits: true,
                minlength: 6,

            }
        },
        messages: {
            first_name: {
                required: "This field is required",
            },
             mobile_number: {
                required: "This field is required",
            },
             email: {
                required: "This field is required",
            },
        },
    });
// validation for forgot Password ends here
    validator = $("div.contact-us form").validate({
        rules: {
            firstname: {
                required: true,
            },
            lastname: {
                required: true,
            },
            email: {
                required: true,
                email: true,
            },
            mobile: {
                digits: true,
                minlength: 10,
                maxlength: 10,
                required: true,
            },
            message: {
                required: true,
            },
        },
        messages: {
            firstname: {
                required: "This field is required",
            },
            lastname: {
                required: "This field is required",
            },
            email: {
                required: "This field is required",
            },
            mobile: {
                required: "This field is required",
            },
            message: {
                required: "This field is required",
            },
        },
    });

//FAQ Plus and Minus js    
    $(".question_block").click(function() {
        $(".question_block").removeClass("active");
        $(this).addClass("active");
    });
    // view all in case report list


/**** js changed on 18/06/2020 *****/
//   mobile menu
    var effect = "slide";
    var option = {direction: "left"};
    var duration = 500;
    $(".menu_bar").click(function() {
        $(".navbar_link").show(effect, option, duration);
    });
    $("nav .close").click(function() {
        $(".navbar_link").hide(effect, option, duration);
    });

// font increase and decrease

    var size = "100%";
    size1 = parseFloat(size);
    
    // font increase

    $(".font_increase").click(function() {
        if ((size1 + 6) <= 110) {
            size2 = size1 += 6;
            size3 = size2 + "%";
            $(".main_section").css("fontSize", size3);
        }
        $(".font_inc_dec li").removeClass("active");
        $(this).addClass("active");
    });

    // font decrease

    $(".font_decrease").click(function() {
        if ((size1 - 6) >= 90) {
            size2 = size1 -= 6;
            size3 = size2  + "%";
            $(".main_section").css("fontSize", size3);
        }
        $(".font_inc_dec li").removeClass("active");
        $(this).addClass("active");
    });

    // font reset

    $(".font_normal").click(function() {
        if ((size1) = 100) {
            size2 = size1  + "%";
            $(".main_section").css("fontSize", size2);
        }
        $(".font_inc_dec li").removeClass("active");
        $(this).addClass("active");
    });
/**** js changed ends on 18/06/2020 ****/





    /********** home page jquery *********/
// case registered list 
$(".registered_right_blk").ready(function() {
    $("#caseRegistered").owlCarousel({
        // autoPlay: 1000,
        loop: true,
        items : 1, // THIS IS IMPORTANT
        nav : true,
        dots : false,
        responsive : {
              480 : { items : 1  }, // from zero to 480 screen width 4 items
              768 : { items : 2  }, // from 480 screen widthto 768 6 items
              1025 : { items : 4   // from 768 screen width to 1024 8 items
              }
          },
    });
});

// view all in case report list

if("#caseReportBlock") {
    $('.case_report_block').ready(function () {
        $('.case_report_list').each(function () {
            $(this).find("li:lt(4)").addClass('shown');
        });
        $('.case_report_list li').not('.shown').hide();
        $('#caseReportBlock .view_all').on('click', function () {
            if(this.innerHTML === "View All") {
                this.innerHTML = "View Less";
            } else {
                this.innerHTML = "View All";
            }
            $(this).parent().next().find("li").not('.shown').toggle(1000);
            $(this).parent().next().find("ul").toggleClass("active");
            
        });
    });
}

// browse the case report List
if('.speciality_block') {
    $(document).ready(function () {
        $('.speciality_block').each(function () {
            $(this).find("li:lt(9)").addClass('shown');
        });
        $('.speciality_block li').not('.shown').hide();
        $('.viewall').on('click', function () {
            $(this).prev().find("li").not('.shown').toggle(1000);
            if(this.innerHTML === "View All") {
                this.innerHTML = "View Less";
            } else {
                this.innerHTML = "View All";
            }
        });
    });
}

// write case report list

if("#writeCaseReport") {
    $("#writeCaseReport").ready(function () {
        $('.write_case_report_list').each(function () {
            $(this).find("li:lt(2)").addClass('shown');
        });
        $('.write_case_report_list li').not('.shown').hide();
        $('#writeCaseReport .view_all').on('click', function () {
            $(this).prev().find("li").not('.shown').toggle(1000);
            if(this.innerHTML === "View All") {
                this.innerHTML = "View Less";
            } else {
                this.innerHTML = "View All";
            }
        });
    });
}

$("#searchIcon").click(function() {
        $("#searchBox input").toggleClass("show");
    });
    //Login App selection js start here
    $(".options").focus(function() {
        $(".options").removeClass("active");
        $(this).addClass("active");
    });
    $(".options").click(function() {
        $(".options").removeClass("active");
        $(this).addClass("active");
    });
    //Login App selection js End here
});

    var mainHeight = $("main .homepage_main_sec").height();
     var mainHeight1 = mainHeight  + "px";
     $("#loginVisitorPage, #ForgetPasswordPage").css("height" , mainHeight1 );
