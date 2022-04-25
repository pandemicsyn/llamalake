/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Job } from './Job';

/**
 * Class level comments on models also get spit out in the schema and rendered in openapi docs.
 */
export type SubmitResponse = {
    jobs?: Array<Job>;
};
