import { Body, Controller, Post } from '@nestjs/common';

@Controller('obd')
export class ObdController {

    @Post()
    async postOBD(@Body() obd: any) {
        console.log(obd);
    }

}
