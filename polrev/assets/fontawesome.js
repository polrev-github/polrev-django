import { library, dom } from '@fortawesome/fontawesome-svg-core'

/*import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
library.add(fas, far, fab)
*/

import {
  faUser,
  faUserCircle,
  faSearch,
  faCalendar,
  faFolderOpen,
  faTag,
  faComments,
  faAngleLeft,
  faAngleRight
} from "@fortawesome/free-solid-svg-icons";

import {
  faGithub,
  faFacebook,
  faTwitter,
  faReddit,
  faMeetup,
  faSlack,
  faTrello,
  faLinkedin
} from "@fortawesome/free-brands-svg-icons";

library.add(
  faUser,
  faUserCircle,
  faSearch,
  faCalendar,
  faFolderOpen,
  faTag,
  faComments,
  faAngleLeft,
  faAngleRight,

  faGithub,
  faFacebook, 
  faTwitter,
  faReddit,
  faMeetup,
  faSlack,
  faTrello,
  faLinkedin
  );

dom.i2svg();
