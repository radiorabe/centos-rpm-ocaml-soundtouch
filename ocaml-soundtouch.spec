Name:     ocaml-soundtouch

Version:  0.1.8
Release:  1
Summary:  OCaml bindings for soundtouch
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-soundtouch
Source0:  https://github.com/savonet/ocaml-soundtouch/releases/download/%{version}/ocaml-soundtouch-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: soundtouch-devel
Requires:      soundtouch

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/soundtouch/META
/usr/lib64/ocaml/soundtouch/soundtouch.a
/usr/lib64/ocaml/soundtouch/soundtouch.cma
/usr/lib64/ocaml/soundtouch/soundtouch.cmi
/usr/lib64/ocaml/soundtouch/soundtouch.cmxa
/usr/lib64/ocaml/soundtouch/soundtouch.mli
/usr/lib64/ocaml/soundtouch/soundtouch.cmx
/usr/lib64/ocaml/soundtouch/libsoundtouch_stubs.a
/usr/lib64/ocaml/stublibs/dllsoundtouch_stubs.so
/usr/lib64/ocaml/stublibs/dllsoundtouch_stubs.so.owner

%description
OCAML bindings for soundtouch


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-soundtouch.spec
