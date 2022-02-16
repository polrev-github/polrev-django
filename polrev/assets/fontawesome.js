import { library, dom } from '@fortawesome/fontawesome-svg-core'

/*import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
library.add(fas, far, fab)
*/

import {
  faUser,
  faUserCircle,
  faChevronRight,
  faSearch,
  faCalendar,
  faFolderOpen,
  faTag,
  faLink,
  faComments,
  faAngleLeft,
  faAngleRight,
  faRssSquare,
  faCalendarPlus
} from "@fortawesome/free-solid-svg-icons";

import {
  faGithub,
  faFacebook,
  faTwitter,
  faReddit,
  faMeetup,
  faSlack,
  faTrello,
  faLinkedin,
  faInstagram,
} from "@fortawesome/free-brands-svg-icons";

library.add(
  faUser,
  faUserCircle,
  faChevronRight,
  faSearch,
  faCalendar,
  faFolderOpen,
  faTag,
  faLink,
  faComments,
  faAngleLeft,
  faAngleRight,
  faRssSquare,
  faCalendarPlus,

  faGithub,
  faFacebook, 
  faTwitter,
  faReddit,
  faMeetup,
  faSlack,
  faTrello,
  faLinkedin,
  faInstagram,
  );

dom.i2svg();
