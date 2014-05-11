# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, RadioField, SelectField, TextAreaField,BooleanField, HiddenField, SubmitField
from wtforms.ext.dateutil.fields import DateField
from wtforms.validators import Required, email



class InvitationForm(Form):
    choices = [(111, u'Canada'), (200, u'San Tome and Principe'), (92, u'Ethiopia'), (86, u'Fidji'), (33, u'Cameroon'),
               (12, u'Burkina Faso'), (99, u'Bosnia and Herzegovina'), (45, u'Liberia'), (121, u'Netherlands'),
               (79, u'Tanzania'), (120, u'Monaco'), (65, u'Palestin'), (57, u'Myanma'), (169, u'South Korea'),
               (155, u'Macao'), (83, u'Turkey'), (216, u'Turkmenistan Republic'), (133, u'France'),
               (227, u'Azerbaidzhan'), (129, u'Slovakia'), (206, u'Nauru'), (123, u'Norway'), (51, u'Malawi'),
               (225, u'Stateless Person'), (128, u'Montenegro'), (150, u'Dominican Republic'), (6, u'Bahrain'),
               (28, u'Indonesia'), (47, u'Libya'), (132, u'Finland'), (115, u'Liechtenstein'), (125, u'Portugal'),
               (52, u'Malaysia'), (14, u'Vietnam'), (205, u'Bermuda Islands'), (202, u'Swasiland'), (42, u'Kuwait'),
               (188, u'Panama'), (170, u'Costa Rica'), (116, u'Luxembourg'), (145, u'Andorra'), (193, u'Gibraltar'),
               (107, u'Ireland'), (110, u'Italy'), (172, u'Nigeria'), (91, u'Ecuador'), (94, u'Australia'),
               (162, u'Bhutan'), (68, u'El Salvador'), (178, u'Tuvalu'), (78, u'Thailand'), (7, u'Belize'),
               (212, u'South Africa Republic'), (77, u'Sierra Leone'), (229, u'Georgia'), (105, u'Denmark'),
               (87, u'Philippines'), (226, u'Moldova'), (54, u'Morocco'), (161, u'Bonaire'), (138, u'Estonia'),
               (19, u'Guinea-Bisau'), (46, u'Lebanon'), (235, u'Uzbekistan'), (38, u'Colombia'), (185, u'Taiwan'),
               (112, u'Cyprus'), (5, u'Barbados'), (50, u'Madagascar'), (189, u'Palau'), (75, u'Sudan'), (59, u'Nepal'),
               (156, u'Republic of Maldives'), (197, u'Cura\u0441ao'), (67, u'Ruanda'), (74, u'Somali'),
               (144, u'Anguilla'), (62, u'The United Arab Emirates'), (106, u'Israel'), (44, u'Lethoto'),
               (71, u'Senegal'), (181, u'\u0421entral-African Republic'), (26, u'Zimbabwe'), (29, u'Jordan'),
               (157, u'Martinique'), (49, u'Mauritania'), (113, u'Latvia'), (139, u'Japan'), (134, u'Croatia'),
               (73, u'Syria'), (191, u'Guadeloupe'), (119, u'Mexico'), (127, u'Serbia'), (76, u'Surinam'),
               (102, u'United Kingdom'), (40, u'Congo'), (184, u'Tahiti'), (66, u'Paraguay'), (15, u'Gabon'),
               (238, u'Czechoslovakia'), (100, u'Brazil'), (194, u'Hongkong'),
               (177, u'Republic of Trinidad and Tobago'), (114, u'Lithuania'), (32, u'Cambodia'), (146, u'Aruba'),
               (173, u'Papua New Guinea'), (96, u'Argentina'), (9, u'Bolivia'), (18, u'Ghana'), (69, u'Saudi Arabia'),
               (130, u'Slovenia'), (192, u'Guatemala'), (20, u'Guinea'), (109, u'Spain'), (64, u'Pakistan'),
               (63, u'Oman'), (31, u'Cabo Verde'), (149, u'Commonwealth of Dominica'), (183, u'French Guiana'),
               (101, u'Vatican'), (122, u'New Zealand'), (30, u'Yemen'), (187, u'Jamaica'), (143, u'Albania'),
               (148, u'Guam'), (27, u'India'), (35, u'Kenya'), (203, u'Saint-Martin'), (201, u'Saint Bartholomew'),
               (135, u'Czech Republic'), (204, u'Eritrea'), (239, u'Saint Lucia'), (199, u'San Marino'),
               (56, u'Mongolia'), (233, u'Norman islands'), (174, u'Peru'), (43, u'Laos'), (8, u'Benin'),
               (198, u'Saipan'), (159, u'Federated States of Micronesia'), (90, u'Sri-Lanka'), (41, u'Cuba'),
               (237, u'Saint Kitts and Nevis'), (80, u'Togo'), (163, u'Vauatu'), (36, u'China'), (218, u'Armenia'),
               (222, u'Ukraine'), (81, u'Tonga'), (11, u'Brunei'), (167, u'Cayman Islands'), (39, u'Comoro Islands'),
               (217, u'Mauritius'), (137, u'Sweden'), (211, u'USSR'), (230, u'British Virgin Islands'), (53, u'Mali'),
               (210, u'Russia'), (98, u'Bulgaria'), (126, u'Romania'), (2, u'Angola'), (88, u'Chad'), (34, u'Qatar'),
               (220, u'Afganistan'), (95, u'Austria'), (55, u'Mozambique'), (84, u'Uganda'), (103, u'Hungary'),
               (60, u'Niger'), (22, u'Democratic Republic Congo'), (179, u'Faeroe Islands'), (4, u'Bangladesh'),
               (152, u'Irak'), (215, u'Belarus'), (153, u'Iran'), (1, u'Algeria'), (236, u'Leeward Islands'),
               (158, u'Marshall Islands'), (89, u'Chile'), (175, u'Puerto Rico'), (97, u'Belgium'), (168, u'Kiribati'),
               (164, u'Haiti'), (17, u'Gambia'), (58, u'Namibia'), (136, u'Switzerland'), (195, u'Grenada'),
               (70, u'Seychelles'), (85, u'Uruguay'), (186, u'Equatorial Guinea'), (23, u'Djibouti'),
               (196, u'Greenland'), (3, u'Antigua and Barbuda'), (176, u'Reunion'), (13, u'Burundi'),
               (61, u'Nicaragua'), (131, u'USA'), (147, u'Bahama islands'), (118, u'Malta'),
               (182, u'Falkland /Malvinian Islands'), (171, u'Cote d`Ivoir'), (190, u'Venezuela'), (232, u'Tibet'),
               (108, u'Iceland'), (25, u'Zambia'), (140, u'Germany'), (151, u'Western Samoa'), (213, u'Kazakhstan'),
               (124, u'Poland'), (231, u'Kyrgyzstan'), (104, u'Greece'), (154, u'Mayotte'), (166, u'Montserrat'),
               (117, u'Macedonia'), (37, u'North Korea'), (165, u'Guyana'), (21, u'Honduras'), (24, u'Egypt'),
               (72, u'Singapore'), (10, u'Botswana'), (228, u'Yugoslavia'), (82, u'Tunis')]
    sex_choices = [('-', u'-'), ('female', u'female'), ('male', u'male')]

    booking_number = StringField('booking_number', validators = [Required()])
    name = StringField('name', validators = [Required()])
    last_name = StringField('last_name', validators = [Required()])
    sex = SelectField('sex', coerce=str, choices=sex_choices,validators = [Required()])
    passport_number = StringField('passport_number', validators = [Required()])
    delivery_needed = BooleanField('if_double')
    citizenship = SelectField('citizenship',coerce=int, choices=sorted(choices), validators = [Required()])
    birth_date = DateField('birthdate',validators=[Required()], display_format='%d-%m-%Y')
    entry_date = DateField('entry-date',validators=[Required()], display_format='%d-%m-%Y')
    exit_date = DateField('exit-date',validators=[Required()], display_format='%d-%m-%Y')
    kids = StringField('kids')
    transport = StringField('transport')
    email = StringField('email',validators=[Required(), email()])
    address = TextAreaField('address')
    cities = TextAreaField('cities')
    if_double = BooleanField('if_double')

class SubmitForm(Form):
    hidden_field = HiddenField('person_data')
    submit = SubmitField('send')