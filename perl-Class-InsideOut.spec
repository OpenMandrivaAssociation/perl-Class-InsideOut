%define upstream_name       Class-InsideOut
%define upstream_version 1.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A safe, simple inside-out object construction kit
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Config)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::File)
BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util) >= 1.90.0
BuildRequires: perl(Storable)
BuildRequires: perl(Test::More) >= 0.450.0
BuildRequires: perl(XSLoader)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(threads)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildArch:  noarch

%description
This is a simple, safe and streamlined toolkit for building inside-out objects.
Unlike most other inside-out object building modules already on CPAN, this
module aims for minimalism and robustness:

* Does not require derived classes to subclass it
* Uses no source filters, attributes or CHECK blocks
* Supports any underlying object type including black-box inheritance
* Does not leak memory on object destruction
* Overloading-safe
* Thread-safe for Perl 5.8.5 or better
* mod_perl compatible
* Makes no assumption about inheritance or initializer needs

It provides the minimal support necessary for creating safe inside-out objects
and generating flexible accessors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CONTRIBUTING Changes LICENSE META.json META.yml MYMETA.yml README examples
%{_mandir}/man3/*
%{perl_vendorlib}/Class

