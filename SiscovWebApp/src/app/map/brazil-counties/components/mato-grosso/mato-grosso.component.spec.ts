import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MatoGrossoComponent } from './mato-grosso.component';

describe('MatoGrossoComponent', () => {
  let component: MatoGrossoComponent;
  let fixture: ComponentFixture<MatoGrossoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MatoGrossoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MatoGrossoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
