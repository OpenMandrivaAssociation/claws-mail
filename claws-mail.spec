%define _disable_ld_no_undefined 1

# There are perl scripts in docs/tools and we don't want to install perl
# modules required by these scripts
%define __noautoreq 'perl(.*)'

Summary:	The user-friendly, lightweight and fast GTK2 based email client
Name:		claws-mail
Version:	3.10.0
Release:	3
Epoch:		1
License:	GPLv3+
Group:		Networking/Mail
Url:		http://www.claws-mail.org
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# from Debian
Patch0:		claws-mail-3.7.6-trashed-read.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	docbook-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1) >= 0.60
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:	pkgconfig(enchant) >= 1.0.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.6
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.6
BuildRequires:	pkgconfig(gnutls) >= 2.2
BuildRequires:	pkgconfig(gobject-2.0) >= 2.6
BuildRequires:	pkgconfig(gthread-2.0) >= 2.6
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.16
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(libgnome-2.0) >= 2.0
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.5
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(NetworkManager) >= 0.6.2
BuildRequires:	pkgconfig(pilot-link)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(valgrind)
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	compface-devel
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	libetpan-devel >= 0.42
BuildRequires:	libxml2-devel
BuildRequires:	openldap-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(python2)

Requires:	compface
Requires:	rootcerts
Requires:	common-licenses
Requires:	aspell-dictionary
# These are dropped
Obsoletes:	%{name}-clamav-plugin < %{EVRD}
Obsoletes:	%{name}-dillo_viewer-plugin < %{EVRD}
Obsoletes:	%{name}-trayicon-plugin < %{EVRD}

%description
Claws-Mail is an e-mail client (and news reader) based on GTK+2, running
on X Window System, and aiming for:
 * Quick response
 * Graceful, and sophisticated interface
 * Easy configuration, intuitive operation
 * Abundant features
The appearance and interface are similar to some popular e-mail clients for
Windows, such as Outlook Express, Becky!, and Datula. The interface is also
designed to emulate the mailers on Emacsen, and almost all commands are
accessible with the keyboard.

The messages are managed by MH format, and you'll be able to use it together
with another mailer based on MH format (like Mew). You can also utilize
fetchmail or/and procmail, and external programs on receiving (like inc or
imget).

This is an improved version over the "bare" sylpheed package. It has
some additional features, and also extends existing features.

Addtitional features include:
    o Scoring
    o Spell checking
    o Return receipts

Improved features include:
    o SMTP Auth
    o Filtering
    o MIME attachments
    o Integrated News reader
    o Automatic mail checking
    o Line-wrapping
    o XML-based addressbook
    o Newly arrived and unread message management
    o Printing
    o GnuPG support
    o Address book supports JPilot, LDAP, LDIF, and vCard data files

For a complete listing of Features: http://www.claws-mail.org/features.php

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/sylpheed-claws
%{_datadir}/appdata/claws-mail.appdata.xml
%{_datadir}/applications/claws-mail.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_iconsdir}/hicolor/*/apps/*.png
%{_docdir}/claws-mail

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Claws Mail
Group:		Development/Other
Requires:	%{name} = %{EVRD}
# Dropped since 3.9.2
Obsoletes:	%{name}-notification-plugin-devel < %{EVRD}
Obsoletes:	%{name}-vcalendar-plugin-devel < %{EVRD}

%description devel
Development files and headers for %{name}.

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/claws-mail.pc

#----------------------------------------------------------------------------

%package acpi-plugin
Summary:	This Claws Mail plugin enables mail notification via LEDs on some laptops
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description acpi-plugin
This plugin for Claws Mail enables mail notification via LEDs on some laptops.

%files acpi-plugin
%{_libdir}/%{name}/plugins/acpi_notifier.so

#----------------------------------------------------------------------------

%package address_keeper-plugin
Summary:	This Claws Mail plugin never forgets e-mail adresses
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description address_keeper-plugin
This plugin for Claws Mail allows saving outgoing addresses to a designated
folder in the address book.Addresses are saved only if not found in the
address book to avoid unwanted duplicates.

%files address_keeper-plugin
%{_libdir}/%{name}/plugins/address_keeper.so

#----------------------------------------------------------------------------

%package att_remover-plugin
Summary:	This Claws Mail plugin enables the removal of attachments
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description att_remover-plugin
This plugin for Claws Mail enables the removal of attachments.

%files att_remover-plugin
%{_libdir}/%{name}/plugins/att_remover.so

#----------------------------------------------------------------------------

%package attachwarner-plugin
Summary:	This Claws Mail plugin enables attachment warnings
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description attachwarner-plugin
This Claws Mail plugin enables attachment warnings.

%files attachwarner-plugin
%{_libdir}/%{name}/plugins/attachwarner.so

#----------------------------------------------------------------------------

%package bogofilter-plugin
Summary:	Bogofilter plugin for Claws Mail
Group:		Networking/Mail
BuildRequires:	bogofilter
Requires:	%{name} = %{EVRD}
Requires:	bogofilter

%description bogofilter-plugin
Enables the scanning of incoming mail received from a POP, IMAP, or LOCAL
account using Bogofilter. It can optionally delete mail identified as spam
or save it to a designated folder. Bogofilter is a pure Bayesian filter,
therefore it has better speed performance than SpamAssassin but might catch
less spam.

%files bogofilter-plugin
%{_libdir}/%{name}/plugins/bogofilter.so

#----------------------------------------------------------------------------

%package bsfilter-plugin
Summary:	This Claws Mail plugin enables spam fitering through bsfilter
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description bsfilter-plugin
Check all messages that are received from an IMAP, LOCAL or POP account
for spam using Bsfilter.

%files bsfilter-plugin
%{_libdir}/%{name}/plugins/bsfilter.so

#----------------------------------------------------------------------------

%package clamd-plugin
Summary:	This Claws Mail plugin enables spam fitering through Clam AntiVirus
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description clamd-plugin
Check all messages that are received from an IMAP, LOCAL or POP account
for spam using Clam AntiVirus.

%files clamd-plugin
%{_libdir}/%{name}/plugins/clamd.so

#----------------------------------------------------------------------------

%package fancy-plugin
Summary:	This Claws Mail plugin renders HTML e-mails through WebKit
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description fancy-plugin
Renders HTML e-mail using the WebKit library.

%files fancy-plugin
%{_libdir}/%{name}/plugins/fancy.so

#----------------------------------------------------------------------------

%package fetchinfo-plugin
Summary:	This Claws Mail plugin inserts headers containing some download information
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description fetchinfo-plugin
This plugin for Claws Mail inserts headers containing some download
information: UIDL, Sylpheeds account name, POP server, user ID
and retrieval time.

%files fetchinfo-plugin
%{_libdir}/%{name}/plugins/fetchinfo.so

#----------------------------------------------------------------------------

%package gdata-plugin
Summary:	This Claws Mail plugin enables access to GData (Google services)
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description gdata-plugin
Plugin to access to GData (Google services). The only currently implemented
feature is inclusion of Google contacts into the address completion.

%files gdata-plugin
%{_libdir}/%{name}/plugins/gdata.so

#----------------------------------------------------------------------------

%package libravatar-plugin
Summary:	This Claws Mail plugin enables libravatar support
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description libravatar-plugin
Plugin to show the profile pictures associated to email addresses provided by
libravatar service ( http://www.libravatar.org ).

%files libravatar-plugin
%{_libdir}/%{name}/plugins/libravatar.so

#----------------------------------------------------------------------------

%package mailmbox-plugin
Summary:	This Claws Mail plugin provides direct access to mbox folders
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description mailmbox-plugin
This Claws Mail plugin provides direct access to mbox folders.

%files mailmbox-plugin
%{_libdir}/%{name}/plugins/mailmbox.so

#----------------------------------------------------------------------------

%package newmail-plugin
Summary:	This Claws Mail plugin can write a summary to a log file
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description newmail-plugin
This Claws Mail plugin can write a summary to a log file upon
receiving new mail. It defaults to ~/Mail/NewLog.

%files newmail-plugin
%{_libdir}/%{name}/plugins/newmail.so

#----------------------------------------------------------------------------

%package notification-plugin
Summary:	This Claws Mail plugin notifies about new mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description notification-plugin
This Claws Mail plugin notifies about new mail.

%files notification-plugin
%{_libdir}/%{name}/plugins/notification.so

#----------------------------------------------------------------------------

%package pdfviewer-plugin
Summary:	This Claws Mail plugin handles PDF and PostScript attachments
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description pdfviewer-plugin
This Claws Mail plugin This plugin handles PDF and PostScript attachments.

%files pdfviewer-plugin
%{_libdir}/%{name}/plugins/pdf_viewer.so

#----------------------------------------------------------------------------

%package perl-plugin
Summary:	Perl interface to Claws Mail's filtering mechanism
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description perl-plugin
This plugin is intended to extend the filtering possibilities of Claws Mail.
It provides a Perl interface to Claws Mail's filtering mechanism, allowing
the use of full Perl power in email filters.

%files perl-plugin
%{_libdir}/%{name}/plugins/perl.so

#----------------------------------------------------------------------------

%package pgpcore-plugin
Summary:	PGP core plugin for Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description pgpcore-plugin
Handles core PGP functions and is a dependency of both the PGP/Inline and
PGP/MIME plugins.

%files pgpcore-plugin
%{_libdir}/%{name}/plugins/pgpcore.so

#----------------------------------------------------------------------------

%package pgpinline-plugin
Summary:	PGP/Inline plugin for Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}
Requires:	%{name}-pgpcore-plugin = %{EVRD}

%description pgpinline-plugin
Handles PGP/Inline signed and/or encrypted mails. You can decrypt mails,
verify signatures or sign and encrypt your own mails.

%files pgpinline-plugin
%{_libdir}/%{name}/plugins/pgpinline.so
%{_libdir}/%{name}/plugins/pgpinline.deps

#----------------------------------------------------------------------------

%package pgpmime-plugin
Summary:	PGP/MIME plugin for Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}
Requires:	%{name}-pgpcore-plugin = %{EVRD}

%description pgpmime-plugin
Handles PGP/MIME signed and/or encrypted mails. You can decrypt mails, verify
signatures or sign and encrypt your own mails.

%files pgpmime-plugin
%{_libdir}/%{name}/plugins/pgpmime.so
%{_libdir}/%{name}/plugins/pgpmime.deps

#----------------------------------------------------------------------------

%package python-plugin
Summary:	Python scriptin access to Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description python-plugin
This plugin offers a Python scripting access to Claws Mail.

%files python-plugin
%{_libdir}/%{name}/plugins/python.so

#----------------------------------------------------------------------------

%package rssyl-plugin
Summary:	This Claws Mail plugin allows you to read your favorite newsfeeds
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description rssyl-plugin
This plugin allows you to read your favorite newsfeeds in Claws Mail.
RSS 1.0, 2.0 and Atom feeds are currently supported.

%files rssyl-plugin
%{_libdir}/%{name}/plugins/rssyl.so

#----------------------------------------------------------------------------

%package smime-plugin
Summary:	S/Mime plugin for Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description smime-plugin
This plugin allows to use S/Mime signatures and encryptions in Claws Mail.

%files smime-plugin
%{_libdir}/%{name}/plugins/smime.so
%{_libdir}/%{name}/plugins/smime.deps

#----------------------------------------------------------------------------

%package spamassassin-plugin
Summary:	Spamassassin-plugin for Claws Mail
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}
Requires:	spamassassin-spamd

%description spamassassin-plugin
Enables the scanning of incoming mail received from a POP, IMAP, or LOCAL
account using SpamAssassin. See README for configuration and set-up info.

%files spamassassin-plugin
%doc src/plugins/spamassassin/README
%{_libdir}/%{name}/plugins/spamassassin.so

#----------------------------------------------------------------------------

%package spam_report-plugin
Summary:	This Claws Mail plugin provides spamreport
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description spam_report-plugin
This Claws Mail plugin provides spamreport.

%files spam_report-plugin
%{_libdir}/%{name}/plugins/spamreport.so

#----------------------------------------------------------------------------

%package tnef_parse-plugin
Summary:	This Claws Mail plugin enables parsing MS-TNEF attachments
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description tnef_parse-plugin
This Claws Mail plugin enables parsing MS-TNEF attachments.

%files tnef_parse-plugin
%{_libdir}/%{name}/plugins/tnef_parse.so

#----------------------------------------------------------------------------

%package vcalendar-plugin
Summary:	This Claws Mail plugin enables vCalendar message handling
Group:		Networking/Mail
Requires:	%{name} = %{EVRD}

%description vcalendar-plugin
This Claws Mail plugin handles the vCalendar format (or rather, the meeting
subset of it). It displays such mails in a nice format, lets you create and
send meetings, and creates a virtual folder with the meetings you have sent
or received.

%files vcalendar-plugin
%{_libdir}/%{name}/plugins/vcalendar.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

%configure2_5x \
	--enable-enchant \
	--enable-jpilot \
	--enable-ldap \
	--enable-crash-dialog \
	--enable-spamassassin-plugin \
	--disable-archive-plugin \
	--enable-ipv6 \
	--enable-compface \
	--enable-gnutls \
	--enable-networkmanager-support \
	--disable-rpath \
	--disable-static

%make LIBTOOL=%{_bindir}/libtool

%check
make check

%install
%makeinstall_std

##remove duplicate man#
rm -rf  %{buildroot}%{_mandir}
## remove unneeded devel files
rm -f %{buildroot}%{_libdir}/%{name}/plugins/*.*a

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
convert %{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m644 %{name}-64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m644 %{name}-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/

cp -a ABOUT-NLS AUTHORS NEWS README* TODO* RELEASE_NOTES tools %{buildroot}%{_docdir}/claws-mail/
rm -f %{buildroot}%{_docdir}/claws-mail/tools/Makefile*

%find_lang %{name}

